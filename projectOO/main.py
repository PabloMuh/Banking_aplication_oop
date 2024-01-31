from auxiliar import *
from operations import *
from bank import *

account_list = []

check = True

while True:
    clear_terminal()
    print("Welcome to Metropolitan Bank")
    print("What do you want to do?")
    print("1 - register an account")
    print("2 - access your account")
    print("3 - support about the operations")
    print("4 - quit the operation")

    choice = int(input("Type your choice: "))

    if choice == 1:
        clear_terminal()
        code = input("Type your New Code Account(made up of letters and numbers): ")
        password = input("Type your New Password: ")
        check_object = account(code,password)

        while any(check_object.code == obj.code for obj in account_list):
            code = input("This code account already exists, please choose another combination: ")
            check_object = account(code,password)

        account_list.append(check_object)
        print("Account created successfully")
        time.sleep(3)
        clear_terminal()

    elif choice == 2:
        clear_terminal()
        code = input("Type your code account: ")
        password = input("Type your Password: ")

        for obj in account_list:
            if code == obj.code and password == obj.password:
                clear_terminal()
                access_account(obj,account_list)
                check = False

        if check:
            print("Account not found, you will be redirected to the home page")
            time.sleep(3)
            clear_terminal()

        check = True
    elif choice == 3:
        clear_terminal()
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - See my history")
        print("4 - Tranference")
        print("5 - See my current balance")
        print("6 - Request a check book")
        print("7 - Pay bills")
        print("8 - Convert my money to another currency")
        print("9 - loan")
        support()

    elif choice == 4:
        clear_terminal()
        print("Thanks for using our services, come back soon!!!")
        break

    else:
        
        clear_terminal()
        print("invalid operation,select another")