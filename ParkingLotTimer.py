parking_lot_list = {
    1:{"Slot" : "1"},
    2:{"Slot" : "2"},
    3:{"Slot" : "3"},
    4:{"Slot" : "4"},
    5:{"Slot" : "5"}
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
    print()