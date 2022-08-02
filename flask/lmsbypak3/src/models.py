from flask_sqlalchemy import SQLAlchemy

#create a database adapter object using SQLAlchemy class
db = SQLAlchemy()

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    teachacct_id = db.Column(db.Integer, unique=True)

    courses = db.relationship('Course', back_populates='teacher')
    #cascade save-update: I think if teacher is deleted, the courses table will have 'null' for teacher_id ??

    def __init__(self, first_name: str, last_name: str, teachacct_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.teachacct_id = teachacct_id
    
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'teachacct_id': self.teachacct_id
        }

class TeachAccount(db.Model):
    __tablename__ = 'teachaccts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(280), unique=True, nullable=False)
    password = db.Column(db.String(280), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

    def __init__(self, username: str, password: str, teacher_id: int):
        self.username = username
        self.password = password
        self.teacher_id = teacher_id
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'teacher_id': self.teacher_id
        }
        #password not shown for security purposes

teacher_student_table = db.Table(
    'teachers_students',
    db.Column(
        'teacher_id', db.Integer,
        db.ForeignKey('teachers.id'),
        primary_key=True
    ),

    db.Column(
        'student_id', db.Integer,
        db.ForeignKey('students.id'),
        primary_key=True
    )
)

class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

student_course_table =db.Table(
    'students_courses',
    db.Column(
        'student_id', db.Integer,
        db.ForeignKey('students.id'),
        primary_key=True
    ),

    db.Column(
        'course_id', db.Integer,
        db.ForeignKey('courses.id'),
        primary_key=True
    )
)

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    period = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.Text, nullable=False)
    
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id')) 
    #one teacher can teach many courses, but one course belongs to one teacher

    assignment = db.relationship('Assignment', back_populates='course')
    teacher = db.relationship('Teacher', back_populates='courses')

    def __init__(self, period: int, subject: str, teacher_id: int):
        self.period = period
        self.subject = subject
        self.teacher_id = teacher_id
    
    def serialize(self):
        return {
            'id': self.id,
            'period': self.period,
            'subject': self.subject,
            'teacher_id': self.teacher_id
        }

student_assignment_table = db.Table(
    'students_assignments',
    db.Column(
        'student_id', db.Integer,
        db.ForeignKey('students.id'),
        primary_key=True
    ),

    db.Column(
        'assignment_id', db.Integer,
        db.ForeignKey('assignments.id'),
        primary_key=True
    ),

    db.Column(
        'received_grade', db.Integer,
        nullable=True
    )
)

class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    #one course can have many assignments, but an assignment can only belong to one course
    max_grade = db.Column(db.Integer)
    #grade is now an attribute of the assignment

    course = db.relationship('Course', back_populates = 'assignment')

    def __init__(self, title: int, course_id: int, max_grade: int):
        self.title = title
        self.course_id = course_id
        self.max_grade= max_grade
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'course_id': self.course_id,
            'max_grade': self.max_grade
        }
#many to many tables
#teacher - student: one teacher can teach many students, one student can have many teachers
#student - course: one student can take many courses, and one course can have many students
#student - assignment: one student can complete many assignments, and one assignment can be completed by many students

