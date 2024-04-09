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
            register()
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
                        print("Your To-Do List:")
                        for key, value in To_Do.items():
                            print(f"{key}: {value}")
                        input("Press any key to exit...")
                        user_menu(username)
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
    print("Your To-Do List:")
    for key, value in To_Do.items():
        print(f"{key}: {value}")
    print("\nAdd new task")
    task=input("Task: ")
    if task in To_Do:
        print("Task is already in your list.")
        add_task(username)
    else:
        task_number = len(To_Do) + 1
        To_Do[task_number]=task
        print("New Task Added") 
        user_menu(username)

def remove_task(username):
    print("Your To-Do List:")
    for key, value in To_Do.items():
        print(f"{key}: {value}")
    print("\nRemoving a Task")
    task_number = int(input("Enter the number of the task to remove: "))
    
    if task_number in To_Do:
        removed_task = To_Do.pop(task_number)
        print(f"Task removed successfully!")
        user_menu(username)
    else:
        print("Invalid task number. No task removed.")
        remove_task(username)

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
                