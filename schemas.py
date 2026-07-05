from pydantic import BaseModel,EmailStr,Field
from datetime import date

    

class EnrollmentCreate(BaseModel):
    enrollment_id   : str = Field(...,min_length=3)
    student_name    : str = Field(...,min_length=3)
    student_email   : EmailStr
    course_name     : str = Field(...,min_length=3)
    course_category : str = Field(...,min_length=3)
    enrollment_date : date
    course_duration : str= Field(...,min_length=3)
    fee_amount      : float = Field(...,gt=0)
    payment_status  : str= Field(...,min_length=3)
    enrollment_status   : str= Field(...,min_length=3)


class EnrollmentUpdate(BaseModel):
    student_name: str | None = None
    student_email: EmailStr | None = None
    course_name: str | None = None
    course_category: str | None = None
    enrollment_date: date | None = None
    course_duration: str | None = None
    fee_amount: float | None = None
    payment_status: str | None = None
    enrollment_status: str | None = None

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    is_active:bool
    
    class Config:
        from_attributes = True        