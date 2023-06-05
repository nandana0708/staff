import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()

#mycursor.execute("CREATE TABLE empdet(emp_id integer UNSIGNED NOT NULL,PRIMARY KEY(emp_id),name VARCHAR(50) NOT NULL,doj DATE NOT NULL)")
#mycursor.execute("CREATE TABLE empleave(leave_no integer UNSIGNED NOT NULL,emp_id integer UNSIGNED NOT NULL,name VARCHAR(20) NOT NULL,PRIMARY KEY(leave_no),FOREIGN KEY(emp_id) REFERENCES empdet(emp_id),leave_from DATE NOT NULL,leave_to DATE NOT NULL)")
#mycursor.execute("CREATE TABLE empatt(att_id integer PRIMARY KEY NOT NULL AUTO_INCREMENT,leave_no VARCHAR(20),emp_id integer UNSIGNED NOT NULL,name VARCHAR(20) NOT NULL,FOREIGN KEY(emp_id) REFERENCES empdet(emp_id),date DATE NOT NULL,day VARCHAR(20) NOT NULL,attendance VARCHAR(50) DEFAULT 'Absent')")
#mycursor.execute("CREATE TABLE holiday(hol_no integer UNSIGNED NOT NULL,PRIMARY KEY(hol_no),hol_name VARCHAR(20) DEFAULT 'public holiday' NOT NULL,date DATE NOT NULL,day VARCHAR(20) NOT NULL)")

