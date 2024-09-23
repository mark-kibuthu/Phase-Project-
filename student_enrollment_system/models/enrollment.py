from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base

class Enrollment(Base):
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    semester = Column(String)

    student = relationship("Student", back_populates="enrollments", overlaps="courses,students")
    course = relationship("Course", back_populates="enrollments", overlaps="students,courses")
