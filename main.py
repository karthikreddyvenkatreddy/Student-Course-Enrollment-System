from fastapi import FastAPI,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database import engine,get_db
import models,schemas,auth
from sqlalchemy.orm import Session
from typing import Optional

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post("/register",response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def register(user_data:schemas.UserCreate,db:Session=Depends(get_db)):
    user_exists = db.query(models.User).filter(models.User.email==user_data.email).first()
    if user_exists:
        raise HTTPException(status_code=400,detail="Email is already registered.")
    
    hashed_pwd = auth.hash_password(user_data.password)
    new_user = models.User(email = user_data.email,hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if user:
        if auth.verify_password(form_data.password,user.hashed_password):
            access_token = auth.create_access_token(data={"sub":user.email})
            return {"access_token":access_token,"token_type":"bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="incorrect email or password",headers={"WWW-Authenticate":"Bearer"})


@app.post("/enrollments")
def createEnrollment(Enrollment_data : schemas.EnrollmentCreate,db:Session=Depends(get_db),current_user: dict = Depends(auth.get_current_user)):
    data_exist = db.query(models.Enrollment).filter(models.Enrollment.enrollment_id==Enrollment_data.enrollment_id).first()
    if data_exist :
        return {"msg":"Enrollment id already found"}
    else :
        db_enrollment = models.Enrollment(**Enrollment_data.model_dump())
        db.add(db_enrollment)
        db.commit()
        return {"msg":f"student added to course with enrollment id {Enrollment_data.enrollment_id}"}


@app.get("/enrollments")
def getallEnrollments(db: Session = Depends(get_db),
                      skip:int = 0,
                      limit:int=10,
                      course_name : Optional[str]=None,
                      payment_status:Optional[str]=None,
                      enrollment_status:Optional[str]=None,
                      current_user: dict = Depends(auth.get_current_user)
                      ):
    query = db.query(models.Enrollment)
    if course_name:
        query = query.filter(models.Enrollment.course_name.ilike(f"%{course_name}%"))
    if payment_status:
        query = query.filter(models.Enrollment.payment_status==payment_status)
    if enrollment_status:
        query = query.filter(models.Enrollment.enrollment_status==enrollment_status)
    return query.offset(skip).limit(limit).all()    
    # allEnrollments_data = db.query(models.Enrollment).offset(skip).limit(limit).all()
    # return allEnrollments_data

@app.get("/enrollments/{enrollment_id}")
def getEnrollmentById(enrollment_id:str,db:Session=Depends(get_db),
                      current_user: dict = Depends(auth.get_current_user)):
    enrollment_data = db.query(models.Enrollment).filter(models.Enrollment.enrollment_id==enrollment_id).first()
    if enrollment_data:
        return enrollment_data
    return {"msg" : f"enrollment id {enrollment_id} not found "}

@app.delete("/enrollments/{enrollment_id}")
def deleteEnrollment(enrollment_id : str,db:Session = Depends(get_db),
                     current_user: dict = Depends(auth.get_current_user)):
    enrollment_data = db.query(models.Enrollment).filter(models.Enrollment.enrollment_id==enrollment_id).first()
    if enrollment_data:
        db.delete(enrollment_data)
        db.commit()
        return {"msg":f"Enrollment deleted with id {enrollment_id}"}
    return {"msg": f"Enrollment not found with id {enrollment_id}"}

@app.put("/enrollments/{enrollment_id}")
def updateEnrollment(enrollment_id : str,
                     new_enrollment_data:schemas.EnrollmentUpdate,
                     db:Session = Depends(get_db),
                     current_user: dict = Depends(auth.get_current_user)):
    db_enrollment_data = db.query(models.Enrollment).filter(models.Enrollment.enrollment_id==enrollment_id).first()
    if db_enrollment_data:
        update_dict = new_enrollment_data.model_dump(exclude_unset=True)
        for key,value in update_dict.items():
            setattr(db_enrollment_data,key,value)
        db.commit()
        db.refresh(db_enrollment_data)
        return db_enrollment_data
    return {"msg": f"Enrollment not found with id {enrollment_id}"}

