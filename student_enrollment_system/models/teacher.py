from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String)

    courses = relationship("Course", back_populates="teacher")
