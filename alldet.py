import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()


def alldet():
    print("Enter following details of the employee whose details need to be searched")
    emp_id=int(input("Enter employment ID: "))
    name=input("Enter full name of employee: ")
    print(" ")
    
    print("Employee details:")
    query="SELECT*FROM empdet where emp_id='%s' and name=%s"
    value=(emp_id,name)
    mycursor.execute(query,value)
    for x in mycursor:
        print(x)
    print(" ")
    
    print("Employee Leave Details:")
    query1="SELECT*FROM empleave where emp_id='%s' and name=%s"
    value1=(emp_id,name)
    mycursor.execute(query1,value1)
    for x in mycursor:
        print(x)
    print(" ")
    
    print("Employee Attendance Details:")
    query2="SELECT*FROM empatt where emp_id='%s' and name=%s"
    value2=(emp_id,name)
    mycursor.execute(query2,value2)
    for x in mycursor:
        print(x)
    print(" ")
    
def del_rec():
    f=open("emp.txt","r")
    r=f.read()
    print(r)
    