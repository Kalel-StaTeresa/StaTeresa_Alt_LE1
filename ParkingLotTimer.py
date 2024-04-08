To_Do = {}

user_info={}

def register():
    print("\nRegister a new account")
    username=input("Enter New username: ")
    if username in user_info:
        print("This username already exists")
    else:
        password=str(input("Enter your password: "))
        if len(password) < 8 :
            print("Password must be atleast 8 characters.")
        else:
            user_info[username]={'password':password}
            print(f"Registration Complete.")

def sign_in():
    print("Sign in an account")
    username=str(input("Enter Username: "))
    password=str(input("Enter Password: "))
    if username in user_info and user_info[username]['password']== password:
        print("Sign in successful")
        user_menu(username)
    else:
        print("Invalid Username/Password")
        return
    
def user_menu(username):
            while True:
                print("\nWelcome to you To-Do List")
                print("1. View Tasks")
                print("2. Add Task")
                print("3. Remove Task")
                print("4. Log out")

                choice=input("\nEnter your choice: ")

                try:
                    choice=int(choice)
                    if choice==1:
                        print()
                    elif choice==2:
                        add_task(username)
                    elif choice==3:
                        remove_task(username)
                    elif choice==4:
                        print("\nLogging off...")
                        menu()
                    else:
                        print("Invalid Input. Please select a number above")
                except ValueError:
                    print("\nInvalid Input. Please enter a number.")

def add_task(username):
    print(To_Do)
    print("\nAdd new task")
    task=input("Task: ")
def remove_task(username):
    pass

def menu():
    while True:
        print("\nMain Menu:")
        print("1. Sign In")
        print("2. Sign up")
        print("3. Exit")

        choice=input("\nEnter your choice: ")

        try:
            choice=int(choice)
            if choice==1:
                sign_in()
            elif choice==2:
                register()
            elif choice==3:
                print("\nExiting Program...")
                exit(0)
            else:
                print("Invalid Input. Please select a number above")
        except ValueError:
            print("\nInvalid Input. Please enter a number.")
menu()
                