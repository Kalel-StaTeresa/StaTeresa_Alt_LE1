import os

def register():
    print("\nRegister a new account")
    username=input("Enter New username: ")
    if username in user_info:
        print("This username already exists")
    else:
        password=str(input("Enter your password: "))
        if len(password) < 4 :
            print("Password must be atleast 4 characters.")
            register()
        else:
            user_info[username] = password
            print(f"Registration Complete.")

def sign_in():
    print("Sign in an account")
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    if username in user_info and user_info[username] == password:
        print("Sign in successful")
        return user_menu(username)
    else:
        print("Invalid Username/Password")
        return None
    
def user_menu(username):
            if username not in to_do:
                to_do[username] = []
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
                        for i, task in enumerate(to_do[username], start=1):
                            print(f"{i}. {task}")
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
    print(f"\nYour To-Do List:")
    for i, task in enumerate(to_do[username], start=1):
        print(f"{i}. {task}")
    print("\nAdd new task")
    task=input("Enter Task: ")
    if task in to_do[username]:
        print("Task is already in your list.")
        add_task(username)
    else:
        to_do[username].append(task)
        print("New Task Added") 
        user_menu(username)

def remove_task(username):
    print("Your To-Do List:")
    for i, task in enumerate(to_do[username], start=1):
        print(f"{i}. {task}")
    print("\nRemoving a Task")
    task_number = int(input("Enter the number of the task to remove: "))
    
    if 1 <= task_number <= len(to_do[username]):
        removed_task = to_do[username].pop(task_number - 1)
        print(f"Task removed successfully!")
        user_menu(username)
    else:
        print("Invalid task number. No task removed.")
        remove_task(username)

user_info={}
to_do = {}

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
                