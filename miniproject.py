import sqlite3
conn=sqlite3.connect("student.db")
v=conn.cursor()
v.execute("PRAGMA foreign_keys=ON")
v.execute("""
             CREATE TABLE IF NOT EXISTS students(
             id integer PRIMARY KEY AUTOINCREMENT,
             name text,
             age integer,
             email text,
             user_id integer,
             FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE           
             )
      """)
v.execute("""
             CREATE TABLE IF NOT EXISTS grades(
             id integer PRIMARY KEY AUTOINCREMENT,
             subject text,
             mark integer,
             grade text,
             student_id integer,
             FOREIGN KEY(student_id)REFERENCES students(id) ON DELETE CASCADE
             
             )
      """)

v.execute("""
             CREATE TABLE IF NOT EXISTS users(
             id integer PRIMARY KEY AUTOINCREMENT,
             username text UNIQUE,
             password text,
             role text
             )
      """)

def register():
    z = input("enter username")
    x = input("enter password")
    c= input("enter ur role")
    if c == "teacher":
        v.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)", (z, x, c))
        conn.commit()
    else:
        v.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)", (z, x, c))
        conn.commit()
        b = input("enter ur name")
        n = input("enter ur age")
        d = input("enter ur email")
        v.execute("INSERT INTO students(name,age,email) VALUES(?,?,?)",(b,n,d))
        conn.commit()

def login():
    z = input("enter username")
    x = input("enter password")
    v.execute("SELECT * FROM users WHERE username=? AND password=?",(z,x))
    y=v.fetchone()
    while True:
       if y:
           role=y[3]
           print("LOGIN SUCCESSFUL")
           break
       else:
           print("invalid credentials")
           z = input("enter username")
           x = input("enter password")
           v.execute("SELECT * FROM users WHERE username=? AND password=?", (z, x))
           y = v.fetchone()
    if role=="teacher":
        t=input("enter student id")
        s=input("enter the subject")
        m=int(input("enter the mark"))
        if m>=90:
            grade="A"
        elif m>=80:
            grade="B"
        elif m >=70:
            grade="C"
        elif m >=60:
            grade="D"
        elif m >=50:
            grade="E"
        else:
            grade="F"
        v.execute("INSERT INTO grades(student_id,subject,mark,grade) VALUES(?,?,?,?)", (t, s, m, grade))
        conn.commit()
    elif role=="student":
        v.execute("""
                 SELECT students.name,students.age,grades.subject,grades.mark,grades.grade
                 FROM students
                 JOIN grades ON students.id = grades.student_id
                 WHERE students.user_id=?

          """,(y[0]))
        print(v.fetchall())
while True:
    print("1)register 2)Login ")
    choice=int(input("enter your choice"))
    if choice==1:
        register()
    elif choice==2:
        login()
    else:
        break
