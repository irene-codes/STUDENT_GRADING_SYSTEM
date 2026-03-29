# Student Grading System

A simple grading system built using Python and SQLite3 
## About the Project
This project allows teachers and students to login using their credentials.
Teachers can add grades for students and students can view their own grades.
The grade is calculated automatically based on the mark entered.
## Database Structure
The project uses 3 tables connected using foreign keys.

users table stores the login credentials and role of every user.
students table stores the personal details of students and is linked to users table.
grades table stores the subject, mark and grade of each student and is linked to students table.

The connection goes like this:
users → students → grades

## How it Works

Teacher:
- Register with username, password and role as teacher
- Login and enter student id, subject and mark
- Grade will be assigned automatically based on the mark

Student:
- Register with username, password, name, age and email
- Login to view personal grades

## Grade Calculation
90 and above - A
80 and above - B
70 and above - C
60 and above - D
50 and above - E
Below 50 - F
