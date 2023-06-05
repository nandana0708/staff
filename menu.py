import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()

import attendance
import employees
import leave
import holiday
import alldet
import menu




def emp_menu():
     while True:
         print("\t\t******************************************************") 
         print("\t\tWELCOME TO EMPLOYEE ATTENDANCE MANAGEMENT SYSTEM(USER)")
         print("\t\t******************************************************") 
         print("\t\tMENU:")
         print("\t\tEnter 1 to open attendance menu")
         print("\t\tEnter 2 to open leave menu")
         print("\t\tEnter 3 to open employee details menu")
         print("\t\tEnter 4 to exit main menu")
         print("\t\t******************************************************")
         choice=int(input("please enter your choice: "))
         if choice==1:
             attendance.emp_attendance()
         elif choice==2:
             leave.emp_leave()
         elif choice==3:
             e1=employees.Employee()
             e1.emp_empdet()
         elif choice==4:
             break
         else:
             print("Invalid option,try again")
            

def ad_menu():
     while True:
         print("\t\t******************************************************") 
         print("\t\tWELCOME TO EMPLOYEE ATTENDANCE MANAGEMENT SYSTEM(ADMIN)")
         print("\t\t******************************************************") 
         print("\t\tMENU:")
         print("\t\tEnter 1 to open attendance menu")
         print("\t\tEnter 2 to open leave menu")
         print("\t\tEnter 3 to open employee details menu")
         print("\t\tEnter 4 to open holidays menu")
         print("\t\tEnter 5 to view all details of an employee")
         print("\t\tEnter 6 to view all deleted employee records")
         print("\t\tEnter 7 to exit main menu")
         print("\t\t******************************************************")
         choice=int(input("please enter your choice: "))
         if choice==1:
             attendance.ad_attendance()
         elif choice==2:
             leave.ad_leave()
         elif choice==3:
             e1=employees.Employee()
             e1.ad_empdet()
         elif choice==4:
             holiday.holiday()
         elif choice==5:
             alldet.alldet()
             print("\tAll details of employee has been displayed")
         elif choice==6:
             alldet.del_rec()
         elif choice==7:
             break
         else:
             print("Invalid option,try again")
   

    
   
    
    
    
    
        
        