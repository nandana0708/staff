import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()

import employees

class Employee:
    def __init__(self):
        self.emp_id="emp_id"
        self.name="name"
        self.doj="doj"
        self.emp_id_new="emp_id_new"
        self.name_new="name_new"
        self.choice="choice"
        self.user_inp="user_inp"
        
    def ad_empdet(self):
        while True:
            print("\t------------------------------------")
            print("\t      EMPLOYEE DETAILS MENU")
            print("\t------------------------------------")
            print("\tEnter 1 to search employee details")
            print("\tEnter 2 to view all employee details")
            print("\tEnter 3 to exit")
            print("\t------------------------------------")
    
            choice=int(input("Enter your choice: "))
            if choice==1:
                Employee.search_empdet(self)
            elif choice==2:
                Employee.viewall_empdet(self)
            elif choice==3:
                break
            else:
                print("\tInvalid Choice,Please try again")
    
    def emp_empdet(self):
        while True:
            print("\t------------------------------------")
            print("\t      EMPLOYEE DETAILS MENU")
            print("\t------------------------------------")
            print("\tEnter 1 to add new employee details")
            print("\tEnter 2 to edit employee details")
            print("\tEnter 3 to delete employee details")
            print("\tEnter 4 to exit")
            print("\t------------------------------------")
            print(" ")
            choice=int(input("Enter your choice: "))
            if choice==1:
                Employee.add_empdet(self)
            elif choice==2:
                Employee.edit_empdet(self)
            elif choice==3:
                Employee.del_empdet(self)
            elif choice==4:
                break
            else:
                print("\tInvalid Choice,Please try again")
        

    def add_empdet(self):
        emp_id=int(input("Enter staff employment ID: "))
        name=input("Enter your full name: ")
        doj=input("Enter date of joining: ")
    
        query="INSERT INTO empdet(emp_id,name,doj) VALUES (%s,%s,%s)"
        value=(emp_id,name,doj)
        mycursor.execute(query,value)
        db.commit()
    
        print("\tYour details have successfully been added to the database")
        print(" ")
    
    def edit_empdet(self):
        print("\t--------------------------------------------")
        print("\t        EDIT EMPLOYEE DETAILS")
        print("\t--------------------------------------------")
        print("\tEnter 1 to edit staff employment ID ")
        print("\tEnter 2 to edit your name ")
        print("\tEnter 3 to edit date of  joining ")
        print("\tEnter 4 to exit from edit employee menu ")
        print("\t--------------------------------------------")
        while True:
            choice=int(input("Please enter your choice: "))
            if choice==1:
                emp_id=int(input("Enter old staff employment ID: "))
                name=input("Enter your name: ")
                emp_id_new=int(input("Enter new staff employment ID: "))
            
                query="UPDATE empdet SET emp_id='%s' WHERE name=%s and emp_id='%s'"
                value=(emp_id_new,name,emp_id)
                mycursor.execute(query,value)
                db.commit()
            
                print("\tFollowing changes have been made in database")
                print(" ")
            elif choice==2:
                emp_id=int(input("Enter staff employment ID: "))
                name=input("Enter old name: ")
                name_new=input("Enter new name: ")
            
                query="UPDATE empdet SET name=%s WHERE name=%s and emp_id='%s'"
                value=(name_new,name,emp_id)
                mycursor.execute(query,value)
                db.commit()
            
                print("\tFollowing changes have been made in database")
                print(" ")
            elif choice==3:
                emp_id=int(input("Enter staff employment ID: "))
                doj=input("Enter new date of joining: ")
            
                query="UPDATE empdet SET doj=%s WHERE emp_id='%s'"
                value=(doj,emp_id)
                mycursor.execute(query,value)
                db.commit()
            
                print("\tFollowing changes have been made in database")
                print(" ")
            elif choice==4:
                break
            else:
                print("\tInvalid choice,Please Try Again")
                print(" ")

    def del_empdet(self):
        user_inp=input("Have you previously entered any leave details in this database?(yes/no): ")
        print(" ")
        if user_inp=='yes':
            f=open("emp.txt","a")
            n=int(input("Enter number of records you want to delete: "))
            for i in range(0,n):
                print("\tAll your detalils will be deleted fom database")
                print(" ")
                emp_id=int(input("Enter staff employment ID: "))
                name=input("Enter your name: ")
                print(" ")
                query="DELETE FROM empatt WHERE emp_id='%s' and name=%s"
                value=(emp_id,name)
                mycursor.execute(query,value)
                
                query1="DELETE FROM empleave WHERE emp_id='%s' and name=%s"
                value1=(emp_id,name)
                mycursor.execute(query1,value1)
        
                query2="DELETE FROM empdet WHERE emp_id='%s' and name=%s"
                value2=(emp_id,name)
                mycursor.execute(query2,value2)
                db.commit()
                
                q=input("Would you like to save deleted records?(yes/no): ")
                if q=='no':
                    f=open("emp.txt","a")
                    f.close()
                    print("\tData has permanently been deleted")
                    print(" ")
                elif q=='yes':
                    doj=input("Enter Date of joining: ")
                    print(" ")
                    rec=str(emp_id)+","+name+","+doj+"\n"
                    f.write(rec)
                    print("\tDeleted data has been saved")
            f.close()

        else:
            f=open("emp.txt","a")
            n=int(input("Enter number of records you want to delete: "))
            for i in range(0,n):
                emp_id=int(input("Enter staff employment ID: "))
                name=input("Enter your name: ")
                
                query="DELETE FROM empatt WHERE emp_id='%s' and name=%s"
                value=(emp_id,name)
                mycursor.execute(query,value)
    
                query="DELETE FROM empdet WHERE name=%s and emp_id='%s'"
                value=(name,emp_id)
                mycursor.execute(query,value)
                db.commit()
                print("Data has been deleted from database")
                
                q=input("Would you like to save deleted records?(yes/no): ")
                if q=='no':
                    f=open("emp.txt","a")
                    f.close()
                    print("\tData has permanently been deleted")
                elif q=='yes':
                    doj=input("Enter Date of joining: ")
                    rec=str(emp_id)+","+name+","+doj+"\n"
                    f.write(rec)
                    print("\tDeleted data has been saved")
            f.close()

        
        print("\tYour details have successfully been deleted from database")

    def search_empdet(self):
        emp_id=int(input("Enter staff employment ID: "))
        name=input("Enter your name: ")
        print(" ")
        query="SELECT*FROM empdet WHERE emp_id='%s' and name=%s"
        value=(emp_id,name)
        mycursor.execute(query,value)
        print("--------------------------------------------")
        for x in mycursor:
            print(x)
        print("--------------------------------------------")

            
    def viewall_empdet(self):
        query="SELECT*FROM empdet"
        mycursor.execute(query)
        print("--------------------------------------------")
        for x in mycursor:
            print(x)
        print("--------------------------------------------")
        print(" ")


# e1=employees.Employee()
# e1.empdet()
#e1.add_empdet()
#e1.edit_empdet()