import mysql.connector as mysql
db = mysql.connect(host='localhost', user='root',
                   password='delwar55555', database='college')
command_handler = db.cursor(buffered=True)

try:
    command_handler.execute("show databases")
except:
    db.rollback()
for x in command_handler:
    print(x)


def admin_session():
    #print("Login Success! Welcome Admin")
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register New Student")
        print("2. Register New Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("Register New Student")
            username = input(str("Student Username: "))
            password = input(str("Student Password: "))
            query_vals = (username, password)
            command_handler.execute(
                "Insert into users(username,password,privilege) values(%s, %s,'student')", query_vals)
            db.commit()
            print(username + " has been registered as student")

        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher Username: "))
            password = input(str("Teacher Password: "))
            query_vals = (username, password)
            command_handler.execute(
                "Insert into users(username,password,privilege) values(%s, %s,'teacher')", query_vals)
            db.commit()  # to save all the changes after query/execution
            print(username + " has been registered as teacher")

        elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student Username: "))
            query_vals = (username, 'student')
            command_handler.execute(
                "delete from users where username = %s and privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:  # check if any row affected
                print("User Not Found")
            else:
                print(username + " has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher Username: "))
            query_vals = (username, 'teacher')
            command_handler.execute(
                "delete from users where username = %s and privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not Found")
            else:
                print(username + " has been deleted")

        elif user_option == '4':
            break

        else:
            print("No valid option found")


def teacher_session():
    while 1:
        print("")
        print("Teacher's Menu")
        print("1. Mark Student Register")
        print("2. View Register")
        print("3. Logout")

        user_option = input(str("Option: "))
        if user_option == '1':
            print("")
            print("Mark Student Register")
            command_handler.execute(
                "select username from users where privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date: DD/MM/YYYY: "))
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                # Present | Absent | Late
                status = input(str("Status for: " + str(record) + " P/A/L: "))
                query_vals = (str(record), date, status)
                command_handler.execute(
                    "insert into attendance (username,date, status) values(%s, %s, %s)", query_vals)
                db.commit()
                print(record + " Marked as " + status)

        elif user_option == '2':
            print("")
            print("Viewing All Student Registered")
            command_handler.execute(
                "select username,date,status from attendance")
            records = command_handler.fetchall()
            for record in records:
                print(record)

        elif user_option == '3':
             break

        else:
             print("No Valid Option Selected")


def student_session(username):
    print("")
    print("Students Menu")
    print("1. View Register")
    print("2. Download Register")
    print("3. Logout")

    user_option = input(str("Option: "))
    if user_option == '1':
        print("Displaying Register")
        username = (str(username),)
        command_handler.execute(
            "select date, username, status from attendance where username = %s", username)
        records = command_handler.fetchall()
        for record in records:
            print(record)

    elif user_option == '2':
        print("Downloading Register")
        username = (str(username),)
        command_handler.execute(
            "select date, username, status from attendance where username = %s", username)
        records = command_handler.fetchall()
        for record in records:
            with open("register.txt", "w") as f:
                f.write(str(records) + "\n")
            f.close()
        print("All Record Saved")
        
    elif user_option == '3':
        print("Exit")

    else:
         print("No Valid Option Selected")


def auth_student():
    print("")
    print("Student's Login")
    print("")
    username = input(str("Username: ")) 
    password = input(str("Password: "))
    query_vals = (username,password)
    command_handler.execute("select username from users where username = %s and password = %s and privilege = 'student' ",query_vals)
    if command_handler.rowcount <=0:
        print("Login Not Recognised")
    else: 
        print("Welcome Student")
        student_session(username)
    
def auth_teacher():
    print("")
    print("Teacher's Login")
    print("")
    username = input(str("Username: ")) 
    password = input(str("Password: "))
    query_vals = (username,password)
    command_handler.execute("select * from users where username = %s and password = %s and privilege = 'teacher' ",query_vals)
    if command_handler.rowcount <=0:
        print("Login Not Recognised")
    else: 
        print("Welcome Teacher")
        teacher_session()
    


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username: "))
    password = input(str("Password: "))
    if username == 'delwar':
        if password == 'delwar55555':
             admin_session()
        else:
            print("Password Incorrect")
    else: 
        print("Login Details Incorrect")
        print("")
    
    
def main():
    while 1:
        print("Welcome to School Management System")
        print("")
        print("1. Login as Student")
        print("2. Login as Teacher")
        print("3. Login as Admin")
        
        user_option = input(str("Option: "))
        if user_option =="1":
            auth_student()
        
        elif user_option =="2":
            auth_teacher()
        
        elif user_option == "3":
            auth_admin()
        else: 
            print("No valid option found")
    
main()
