import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click
from db.setup import init_db, SessionLocal
from models.student import Student
from models.course import Course
from models.teacher import Teacher
from models.enrollment import Enrollment

def get_session():
    """Get a new database session."""
    return SessionLocal()

@click.command()
def initdb():
    """Initialize the database."""
    engine = get_session().get_bind()
    init_db(engine)
    click.echo("Database initialized!")

# CRUD operations

def add_student():
    session = get_session()
    name = click.prompt("Enter student name")
    major = click.prompt("Enter student major")
    year = click.prompt("Enter student year", type=int)

    student = Student(name=name, major=major, year=year)
    session.add(student)
    session.commit()
    click.echo(f"Student {name} added!")

def add_teacher():
    session = get_session()
    name = click.prompt("Enter teacher name")
    department = click.prompt("Enter teacher department")

    teacher = Teacher(name=name, department=department)
    session.add(teacher)
    session.commit()
    click.echo(f"Teacher {name} added!")

def add_course():
    session = get_session()
    name = click.prompt("Enter course name")
    credits = click.prompt("Enter number of credits", type=int)
    
    teachers = session.query(Teacher).all()
    if not teachers:
        click.echo("No teachers available. Please add a teacher first.")
        return
    
    click.echo("Available teachers:")
    for teacher in teachers:
        click.echo(f"{teacher.id}: {teacher.name} (Department: {teacher.department})")
    
    teacher_id = click.prompt("Enter teacher ID for the course", type=int)
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        click.echo("Teacher ID not found.")
        return
    
    new_course = Course(name=name, credits=credits, teacher_id=teacher_id)
    session.add(new_course)
    session.commit()
    click.echo(f"Course '{name}' added successfully.")

def update_student():
    session = get_session()
    students = session.query(Student).all()
    if not students:
        click.echo("No students found.")
        return
    
    click.echo("Available students:")
    for student in students:
        click.echo(f"{student.id}: {student.name} (Major: {student.major}, Year: {student.year})")
    
    student_id = click.prompt("Enter the ID of the student to update", type=int)
    student = session.query(Student).filter_by(id=student_id).first()
    
    if not student:
        click.echo("Student ID not found.")
        return
    
    name = click.prompt(f"Enter new name for student (current: {student.name})", default=student.name)
    major = click.prompt(f"Enter new major for student (current: {student.major})", default=student.major)
    year = click.prompt(f"Enter new year for student (current: {student.year})", default=student.year, type=int)
    
    student.name = name
    student.major = major
    student.year = year
    
    session.commit()
    click.echo(f"Student {student_id} updated successfully.")

def update_teacher():
    session = get_session()
    teachers = session.query(Teacher).all()
    if not teachers:
        click.echo("No teachers found.")
        return
    
    click.echo("Available teachers:")
    for teacher in teachers:
        click.echo(f"{teacher.id}: {teacher.name} (Department: {teacher.department})")
    
    teacher_id = click.prompt("Enter the ID of the teacher to update", type=int)
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    
    if not teacher:
        click.echo("Teacher ID not found.")
        return
    
    name = click.prompt(f"Enter new name for teacher (current: {teacher.name})", default=teacher.name)
    department = click.prompt(f"Enter new department for teacher (current: {teacher.department})", default=teacher.department)
    
    teacher.name = name
    teacher.department = department
    
    session.commit()
    click.echo(f"Teacher {teacher_id} updated successfully.")

def update_course():
    session = get_session()
    courses = session.query(Course).all()
    if not courses:
        click.echo("No courses found.")
        return
    
    click.echo("Available courses:")
    for course in courses:
        click.echo(f"{course.id}: {course.name} (Credits: {course.credits})")
    
    course_id = click.prompt("Enter the ID of the course to update", type=int)
    course = session.query(Course).filter_by(id=course_id).first()
    
    if not course:
        click.echo("Course ID not found.")
        return
    
    name = click.prompt(f"Enter new name for course (current: {course.name})", default=course.name)
    credits = click.prompt(f"Enter new credits for course (current: {course.credits})", default=course.credits, type=int)
    
    course.name = name
    course.credits = credits
    
    session.commit()
    click.echo(f"Course {course_id} updated successfully.")

def delete_student():
    session = get_session()
    students = session.query(Student).all()
    if not students:
        click.echo("No students found.")
        return
    
    click.echo("Available students:")
    for student in students:
        click.echo(f"{student.id}: {student.name} (Major: {student.major}, Year: {student.year})")
    
    student_id = click.prompt("Enter the ID of the student to delete", type=int)
    student = session.query(Student).filter_by(id=student_id).first()
    
    if not student:
        click.echo("Student ID not found.")
        return
    
    session.delete(student)
    session.commit()
    click.echo(f"Student {student_id} deleted successfully.")

def delete_teacher():
    session = get_session()
    teachers = session.query(Teacher).all()
    if not teachers:
        click.echo("No teachers found.")
        return
    
    click.echo("Available teachers:")
    for teacher in teachers:
        click.echo(f"{teacher.id}: {teacher.name} (Department: {teacher.department})")
    
    teacher_id = click.prompt("Enter the ID of the teacher to delete", type=int)
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    
    if not teacher:
        click.echo("Teacher ID not found.")
        return
    
    session.delete(teacher)
    session.commit()
    click.echo(f"Teacher {teacher_id} deleted successfully.")

def delete_course():
    session = get_session()
    courses = session.query(Course).all()
    if not courses:
        click.echo("No courses found.")
        return
    
    click.echo("Available courses:")
    for course in courses:
        click.echo(f"{course.id}: {course.name} (Credits: {course.credits})")
    
    course_id = click.prompt("Enter the ID of the course to delete", type=int)
    course = session.query(Course).filter_by(id=course_id).first()
    
    if not course:
        click.echo("Course ID not found.")
        return
    
    session.delete(course)
    session.commit()
    click.echo(f"Course {course_id} deleted successfully.")

def view_students():
    session = get_session()
    students = session.query(Student).all()
    if not students:
        click.echo("No students found.")
        return
    
    click.echo("Students:")
    for student in students:
        click.echo(f"ID: {student.id}, Name: {student.name}, Major: {student.major}, Year: {student.year}")

def view_teachers():
    session = get_session()
    teachers = session.query(Teacher).all()
    if not teachers:
        click.echo("No teachers found.")
        return
    
    click.echo("Teachers:")
    for teacher in teachers:
        click.echo(f"ID: {teacher.id}, Name: {teacher.name}, Department: {teacher.department}")

def view_courses():
    session = get_session()
    courses = session.query(Course).all()
    if not courses:
        click.echo("No courses found.")
        return
    
    click.echo("Courses:")
    for course in courses:
        click.echo(f"ID: {course.id}, Name: {course.name}, Credits: {course.credits}")

def enroll_student():
    session = get_session()
    
   
    students = session.query(Student).all()
    if not students:
        click.echo("No students found.")
        return
    
    click.echo("Available students:")
    for student in students:
        click.echo(f"{student.id}: {student.name}")
    
   
    student_id = click.prompt("Enter the ID of the student to enroll", type=int)
    student = session.query(Student).filter_by(id=student_id).first()
    
    if not student:
        click.echo("Student ID not found.")
        return
    
    
    courses = session.query(Course).all()
    if not courses:
        click.echo("No courses available.")
        return
    
    click.echo("Available courses:")
    for course in courses:
        click.echo(f"{course.id}: {course.name}")
 
    course_id = click.prompt("Enter the ID of the course to enroll in", type=int)
    course = session.query(Course).filter_by(id=course_id).first()
    
    if not course:
        click.echo("Course ID not found.")
        return

    
    semester = click.prompt("Enter the semester (e.g., Fall 2023, Spring 2024)", type=str)

   
    existing_enrollment = session.query(Enrollment).filter_by(
        student_id=student.id,
        course_id=course.id,
        semester=semester
    ).first()
    
    if existing_enrollment:
        click.echo(f"Student is already enrolled in this course for {semester}.")
        return
    
    
    enrollment = Enrollment(student_id=student.id, course_id=course.id, semester=semester)
    session.add(enrollment)
    session.commit()
    
    click.echo(f"Student {student.name} enrolled in course '{course.name}' for {semester}.")



def menu():
    """Display the main menu."""
    while True:
        click.echo("\nStudent Enrollment System Menu:")
        click.echo("1. Add Student")
        click.echo("2. Add Teacher")
        click.echo("3. Add Course")
        click.echo("4. View Students")
        click.echo("5. View Teachers")
        click.echo("6. View Courses")
        click.echo("7. Update Student")
        click.echo("8. Update Teacher")
        click.echo("9. Update Course")
        click.echo("10. Delete Student")
        click.echo("11. Delete Teacher")
        click.echo("12. Delete Course")
        click.echo("13. Enroll Student")
        click.echo("14. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            add_course()
        elif choice == '4':
            view_students()
        elif choice == '5':
            view_teachers()
        elif choice == '6':
            view_courses()
        elif choice == '7':
            update_student()
        elif choice == '8':
            update_teacher()
        elif choice == '9':
            update_course()
        elif choice == '10':
            delete_student()
        elif choice == '11':
            delete_teacher()
        elif choice == '12':
            delete_course()
        elif choice == '13':
            enroll_student()
        elif choice == '14':
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice, please try again.")

@click.group()
def cli():
    """CLI for Student Enrollment System."""
    pass

cli.add_command(initdb)

@click.command(name='default')
def default():
    """Run the main menu."""
    menu()


cli.add_command(default)


if __name__ == "__main__":
    default()