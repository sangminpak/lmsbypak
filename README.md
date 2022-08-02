# Title

Learning Management System

# Description

When I was using Google Classroom daily, every period during the pandemic, I noticed some things that can be improved. I also wanted to create my own app to keep track of students' grades, so I decided to create a learning management system (LMS).

My LMS is consisted of 5 entities: assignments, courses, students, teachaccts (teacher's account that holds username and password), and teachers. Grade is an attribute of the relationship between student and assignment, and lives in the 'many to many' column.

# API Reference Table of endpoint paths, methods, parameters

Each entity has GET, POST, DELETE requests. Only teachaccts entity has PUT request to update username and password.

List of endpoint paths, methods, parameters - to be added later.


# Retrospective answering of the following questions:

1. How did the project's design evolve over time?
- I struggled since the beginning what to do with 'grades.' At first, I created my ER diagram with grade as an attribute of assignments entity. As I was coding in SQL, I felt that that would not make sense because the grade attribute needs to be linked to the student as well, not just the assignment (because the student will receive a certain grade in an assignment). However, when I was creating ORM, I realized that it would be best if grade attribute would be connected to the relationship between assignment and student, so that it can be tracked in the many-to-many table between those two entities.

2. Did you choose to use an ORM or raw SQL? Why?
- I chose ORM for two reasons; one, ORM part had very detailed directions (Flask exercise), and second, I wanted to choose a harder one so that I can learn more. I especially wanted to tackle Flask because I was still struggling to understand what it is and how it's used.

3. What future improvements are in store, if any?
- First, creating API requests are still in process. I also want to check if the relationships are actually created correctly. In the long term, I would love to put the front-end piece so that I can actually enter students' grades and keep track of them using an app with UI.