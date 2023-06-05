import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="staff"
    )
    

mycursor=db.cursor()


import menu

while True:
    print("\t\t-------------")
    print("\t\t    ADMIN")
    print("\t\t    USER")
    print("\t\t-------------")
    print(" ")

    choice=int(input("enter 1 for ADMIN and 2 for USER and 3 to exit: "))
    if choice==1:
        password=input("ENTER PASSWORD TO ACCESS ADMIN DATABASE: ")
        if password=='admin':
            menu.ad_menu()
        else:
            print("\tWRONG PASSWORD,PLEASE TRY AGAIN")
    elif choice==2:
        password=input("ENTER PASSWORD TO ACCESS USER DATABASE: ")
        if password=='user':
            menu.emp_menu()
        else:
            print("\tWRONG PASSWORD,PLEASE TRY AGAIN")
    elif choice==3:
        break
    else:
        print("PLEASE ENTER ONE OF THE ABOVE OPTIONS")
        

    



    