import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()

def holiday():
    while True:
        print("\t------------------------------")
        print("\t        HOLIDAY MENU")
        print("\t------------------------------")
        print("\tEnter 1 to add holidays")
        print("\tEnter 2 to view all holidays")
        print("\tEnter 3 to edit holidays")
        print("\tEnter 4 to exit")
        print("\t------------------------------")
    
        choice=int(input("Please enter one of the above choices: "))
        if choice==1:
            add_hol()
        elif choice==2:
            viewall_hol()
        elif choice==3:
            edit_hol()
        elif choice==4:
            break
        else:
            print("\tInvalid Choice,Please try again")
            

def add_hol():
    hol_no=int(input("Enter holiday number: "))
    date=input("Enter date of holiday: ")
    day=input("Enter day of holiday: ")
    
    query="INSERT INTO holiday(hol_no,date,day) VALUES (%s,%s,%s)"
    value=(hol_no,date,day)
    mycursor.execute(query,value)
    query1="UPDATE empatt SET attendance='public holiday' WHERE day=%s and date=%s"
    value1=(day,date)
    mycursor.execute(query1,value1)
    db.commit()

    print("\tHoliday has successfully been added to the database")
    
def edit_hol():
    print("\t------------------------------------")
    print("\t       EDIT HOLIDAY MENU")
    print("\t------------------------------------")
    print("\tEnter 1 to edit holiday date: ")
    print("\tEnter 2 to edit day of holiday: ")
    print("\tEnter 3 to exit edit holiday menu: ")
    print("\t------------------------------------")
    while True:
        choice=int(input("Please enter your choice"))
        if choice==1:
            date=input("Enter old holiday date: ")
            day=input("Enter day of holiday")
            date_new=input("Enter new holiday date: ")
            
            query="UPDATE holiday SET date=%s WHERE date=%s and day=%s"
            value=(date_new,date,day)
            mycursor.execute(query,value)
            
            query1="UPDATE empatt SET date=%s WHERE date=%s and day=%s"
            value1=(date_new,date,day)
            mycursor.execute(query1,value1)
            db.commit()
            
            print("\tFollowing changes have been updated in database")
        elif choice==2:
            date=input("Enter holiday date: ")
            day=input("Enter old day of holiday")
            day_new=input("Enter new day of holiday: ")

            query="UPDATE holiday SET day=%s WHERE day=%s and date=%s"
            value=(day_new,day,date)
            mycursor.execute(query,value)
            
            query1="UPDATE empatt SET day=%s WHERE day=%s and date=%s"
            value1=(day_new,day,date)
            mycursor.execute(query1,value1)
            db.commit()
            
            print("\tFollowing changes have been updated in database")
        elif choice==3:
            break
        else:
            print("\tInvalid Choice,Please Try again")
    
def viewall_hol():
    query="SELECT*FROM holiday"
    mycursor.execute(query)
    print("--------------------------------------------")
    for x in mycursor:
        print(x)
    print("--------------------------------------------")   

        

    
    
 
            

    
            
    