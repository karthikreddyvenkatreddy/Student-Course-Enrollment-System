from database import Base
from sqlalchemy import Column,Integer,String,Date,Float,Boolean

class Enrollment(Base):
    __tablename__ = "enrollments"
    id              = Column(Integer,primary_key=True,autoincrement=True,index=True)
    enrollment_id   = Column(String(50),unique=True,nullable=False,index=True)
    student_name    = Column(String(50),nullable=False)
    student_email   = Column(String(50),nullable=False)
    course_name     = Column(String(50),nullable=False)
    course_category = Column(String(50),nullable=False)
    enrollment_date = Column(Date,nullable=False)
    course_duration = Column(String(50),nullable=False)
    fee_amount      = Column(Float,nullable=False)
    payment_status  = Column(String(50),default="pending")
    enrollment_status   = Column(String(50),default="active")

class User(Base):
    __tablename__ = "users"

    id   = Column(Integer,primary_key=True,autoincrement=True)
    email= Column(String(50),unique=True,nullable=False,index=True)
    hashed_password=Column(String(500),nullable=False)
    is_active = Column(Boolean,default=True)
