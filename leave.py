import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()

def emp_leave():
    while True:
        print("\t---------------------------------")
        print("\t          LEAVE MENU             ")
        print("\t---------------------------------")
        print("\tEnter 1 to add leave details")
        print("\tEnter 2 to edit leave details")
        print("\tEnter 3 to delete leave details")
        print("\tEnter 4 to exit")
        print("\t---------------------------------")
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_leavedet()
        elif choice==2:
            edit_leavedet()
        elif choice==3:
            del_leavedet()
        elif choice==4:
            break
        else:
            print("\tInvalid Choice,Please try again")
            
def add_leavedet():
    print(" ")
    leave_no=input("Enter leave no: ")
    emp_id=int(input("enter employment ID:"))
    name=input("Enter your full name: ")
    leave_from=input("Enter leave starting date (in YYYY/MM/DD format): ")
    leave_to=input("Enter leave ending date (in YYYY/MM/DD format: ")
    
    query="INSERT INTO empleave(leave_no,emp_id,name,leave_from,leave_to) VALUES (%s,%s,%s,%s,%s)"
    value=(leave_no,emp_id,name,leave_from,leave_to)
    mycursor.execute(query,value)
    query1="UPDATE empatt SET attendance='leave' WHERE leave_no=%s and emp_id='%s'"
    value1=(leave_no,emp_id)
    mycursor.execute(query1,value1)
    db.commit()
    
    print("\tYour Leave details have successfully been added to database")
    print(" ")

def edit_leavedet():
    print("\t---------------------------------")
    print("\t       EDIT LEAVE MENU")
    print("\t---------------------------------")
    print("\tEnter 1 to edit leave start date")
    print("\tEnter 2 to edit leave end date")
    print("\tEnter 3 to exit edit leave menu")
    print("\t---------------------------------")
    while True:
        choice=int(input("Please enter your choice: "))
        if choice==1:
            emp_id=int(input("enter ID:"))
            leave_from=input("Enter your old leave start date: ")
            leave_from_new=input("enter new leave start date: ")
            
            query="UPDATE empleave SET leave_from=%s WHERE leave_from=%s and emp_id='%s'"
            value=(leave_from_new,leave_from,emp_id)
            mycursor.execute(query,value)
            db.commit()
            
            print("Following changes have been updated in database")
        elif choice==2:
            emp_id=int(input("enter ID:"))
            leave_to=input("Enter old leave end date: ")
            leave_to_new=input("enter new leave end date: ")
            
            query="UPDATE empleave SET leave_to=%s WHERE emp_id='%s' and leave_to=%s"
            value=(leave_to_new,emp_id,leave_to)
            mycursor.execute(query,value)
            db.commit()
            
            print("Following changes have been updated in database")
        elif choice==3:
            break
        else:
            print("\tInvalid Choice,Please Try again")
            
def del_leavedet():
    emp_id=int(input("Enter staff employment ID: "))
    leave_no=input("Enter leave number: ")
    
    query="DELETE FROM empleave WHERE leave_no=%s and emp_id='%s'"
    value=(leave_no,emp_id)
    mycursor.execute(query,value)
    db.commit()
    
    print("\tYour leave details have successfully been deleted from database")
    
def ad_leave():
    while True:
        print("\t---------------------------------")
        print("\t          LEAVE MENU             ")
        print("\t---------------------------------")
        print("\tEnter 1 to search leave details")
        print("\tEnter 2 to view all leave details")
        print("\tEnter 3 to exit")
        print("\t---------------------------------")
        choice=int(input("Enter your choice: "))
        if choice==1:
            search_leavedet()
        elif choice==2:
            viewall_leavedet()
        elif choice==3:
            break
        else:
            print("\tInvalid Choice,Please try again")
            
def search_leavedet():
    emp_id=int(input("enter ID:"))
    name=input("Enter Name of employee: ")

    query="SELECT*FROM empleave WHERE emp_id='%s' and name=%s"
    value=(emp_id,name)
    mycursor.execute(query,value)
    print("---------------------------------------------------------------------")
    for x in mycursor:
        print(x)
    print("---------------------------------------------------------------------")
        
def viewall_leavedet():
    query="SELECT*FROM empleave"
    mycursor.execute(query)
    print("---------------------------------------------------------------------")
    for x in mycursor:
        print(x)
    print("---------------------------------------------------------------------")    

    
    
    
    
    