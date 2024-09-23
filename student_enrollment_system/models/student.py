from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    major = Column(String)
    year = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="student", overlaps="courses,student")
    courses = relationship("Course", secondary="enrollments", back_populates="students", overlaps="enrollments,student")
