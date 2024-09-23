from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    credits = Column(Integer)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course", overlaps="students,courses")
    students = relationship("Student", secondary="enrollments", back_populates="courses", overlaps="enrollments,courses")
