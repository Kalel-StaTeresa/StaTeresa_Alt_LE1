import os

inventory = {
    1:{}
}

user_info={}


def register():
    print("\nRegister a new account")
    username=input("Enter New username: ")
    if username in user_info:
        print("This username already exists")
    else:
        password=str(input("Enter your password: "))
        if len(password) < 6 :
            print("Password must be atleast 6 characters.")
        else:
            user_info[username]={'password':password}
            print(f"Registration Complete.")

def sign_in():
    print("Sign in an account")
    username=str(input("Enter username: "))
    password=str(input("Enter Password: "))
    if username in user_info and user_info[username]['password']== password:
        print("Sign in successful")
        user_menu(username)
    else:
        print("Invalid Username/Password")
        return
    
def user_menu(username):
            while True:
                print("\nWelcome")
                print("1. ")
                print("2. ")
                print("3. ")
                print("4. ")
                print("5. Log out")

                choice=input("\nEnter your choice: ")

                try:
                    choice=int(choice)
                    if choice==1:
                        print()
                    elif choice==2:
                        print()
                    elif choice==3:
                        print()
                    elif choice==4:
                        print()
                    elif choice==5:
                        print("\nLogging off...")
                        menu()
                    else:
                        print("Invalid Input. Please select a number above")
                except ValueError:
                    print("\nInvalid Input. Please enter a number.")

    
def admin_log():
    print("Sign in an account")
    username=str(input("Enter username: "))
    password=str(input("Enter Password: "))
    if username=="admin" and password=="adminpass":
        print("Admin Log in Successful")
        admin_menu()
    else:
        print("Incorrect Admin Username/Password")
        return
    
def admin_menu():
        while True:
            print("\nAdmin Settings")
            print("1. ")
            print("2. ")
            print("3. ")
            print("4. ")
            print("5. Exit")

            choice=input("\nEnter your choice: ")

            try:
                choice=int(choice)
                if choice==1:
                    print()
                elif choice==2:
                    print()
                elif choice==3:
                    print()
                elif choice==4:
                    print()
                elif choice==5:
                    print("\nLogging off...")
                    menu()
                else:
                    print("Invalid Input. Please select a number above")
            except ValueError:
                print("\nInvalid Input. Please enter a number.")
    
def menu():
    while True:
        print("\nMain Menu:")
        print("1. ")
        print("2. Sign In")
        print("3. Sign up")
        print("4. Admin Log in")
        print("5. Exit")

        choice=input("\nEnter your choice: ")

        try:
            choice=int(choice)
            if choice==1:
                print()
            elif choice==2:
                sign_in()
            elif choice==3:
                register()
            elif choice==4:
                admin_log()
            elif choice==5:
                print("\nExiting Program...")
                exit(0)
            else:
                print("Invalid Input. Please select a number above")
        except ValueError:
            print("\nInvalid Input. Please enter a number.")
menu()
                