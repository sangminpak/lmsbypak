# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    title = db.Column(db.Text, nullable=False, unique=True)
    max_grade = db.Column(db.Numeric, server_default=db.FetchedValue())

    students = db.relationship('Student', secondary='students_assignments', backref='assignments')



class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    period = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.Text, nullable=False)
    assignment_id = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer)

    students = db.relationship('Student', secondary='students_courses', backref='courses')
    teachers = db.relationship('Teacher', secondary='students_teachers', backref='courses')



class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    received_grade = db.Column(db.Numeric)
    student_id = db.Column(db.ForeignKey('students.id'))
    assignment_id = db.Column(db.ForeignKey('assignments.id'))

    assignment = db.relationship('Assignment', primaryjoin='Grade.assignment_id == Assignment.id', backref='grades')
    student = db.relationship('Student', primaryjoin='Grade.student_id == Student.id', backref='grades')



class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)



t_students_assignments = db.Table(
    'students_assignments',
    db.Column('student_id', db.ForeignKey('students.id'), primary_key=True, nullable=False),
    db.Column('assignment_id', db.ForeignKey('assignments.id'), primary_key=True, nullable=False)
)



t_students_courses = db.Table(
    'students_courses',
    db.Column('student_id', db.ForeignKey('students.id'), primary_key=True, nullable=False),
    db.Column('course_id', db.ForeignKey('courses.id'), primary_key=True, nullable=False)
)



t_students_teachers = db.Table(
    'students_teachers',
    db.Column('student_id', db.ForeignKey('courses.id'), primary_key=True, nullable=False),
    db.Column('teacher_id', db.ForeignKey('teachers.id'), primary_key=True, nullable=False)
)



class Teachacct(db.Model):
    __tablename__ = 'teachaccts'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)



class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    teachacct_id = db.Column(db.Integer, unique=True)
