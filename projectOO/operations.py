from auxiliar import *
import random

class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass
class account():
    def __init__(self,code,password):
        self.code = code
        self.password = password
        self.balance = 0
        self.history = []
        self.bill = []
        self.value = []
        self.currency = 1

    def validatevalue(self, value):
        try:
            value = int(value)
        except ValueError:
            raise AbortTransaction('Value must be an integer')
        if value <= 0:
            raise AbortTransaction('Value must be positive')
        return value
    
    def checkPassword(self):
        password = input("Enter your password to confirm the transaction: ")
        if password != self.password:
            raise AbortTransaction("The Password is incorrect")

    def deposit(self, value):
        value = self.validatevalue(value)
        self.checkPassword()
        self.balance += value
        self.balance = round(self.balance, 2)
        self.history.append(f"You made a deposit of {value}. Your account balance after this is {self.balance}")
        print(f"You make a deposit of {value} in your account. Your account balance now is {self.balance}")

    def withdraw(self,value):
        value = self.validatevalue(value)
        self.checkPassword()
        if self.balance >= value:
            self.balance = self.balance - value
            self.balance = round(self.balance, 2)
            self.history.append(f"You realize a withdraw of {value}. Your accout balance after this is {self.balance}")
            print(f"You make a withdraw of {value} in your account. Your account balance now is {self.balance}")
        else:
            raise AbortTransaction("You are unable to withdraw this value")

    def show_transactions(self):
        self.checkPassword()
        i = 1
        for transactions in self.history:
            print(f"{i} - {transactions}")
            i += 1

    def transfer(self,account_list):
            check_transfer = False

            code = input("Enter the account code you want to transfer:")
            if code == self.code:
                raise AbortTransaction("You can't transfer to your own account")
            for destine in account_list:
                if code == destine.code:
                    check_transfer = True
                    break  

            if check_transfer:
                original = input("How much is the value of transfer: ")
                original = self.validatevalue(original)
                self.checkPassword()
                if original <= self.balance:
                    if self.currency == 1 and destine.currency == 2:
                        value = convert_currency(original, 'BRL', 'USD')
                    elif self.currency == 1 and destine.currency == 3:
                        value = convert_currency(original, 'BRL', 'EUR')
                    elif self.currency == 2 and destine.currency == 1: 
                        value = convert_currency(original, 'USD', 'BRL')
                    elif self.currency == 2 and destine.currency == 3:
                        value = convert_currency(original, 'USD', 'EUR')
                    elif self.currency == 3 and destine.currency == 1:
                        value = convert_currency(original, 'EUR', 'BRL')
                    elif self.currency == 3 and destine.currency == 2:
                        value = convert_currency(original, 'EUR', 'USD')
                    else:
                        value = original
                    self.balance -= original
                    self.balance = round(self.balance, 2)
                    destine.balance += value
                    destine.balance = round(destine.balance, 2)
                    self.history.append(f"You transferred {value} to account {destine.code}")
                    destine.history.append(f"You received {value} of the account {self.code}")
                    print(f"Transfer of {round(value,2)} to account {destine.code} completed successfully.")
                else:
                    raise AbortTransaction("You do not have sufficient funds for this transfer.")          
            else:
                clear_terminal()
                raise AbortTransaction("Account not found, you will be redirected to your home page!!!")

    def bills(self):
        check = False
        if self.bill:
            check = True
            print(self.bill[0])
            choice = input("Do you want pay the bill? y/n : ")
            choice = choice.lower()

            if choice == "y":
                value = self.value[0]
                code_bill = input("Enter the surname of bill: ")
            else:
                return
        else:        
            code_bill = input("Enter the bar code of your bill: ")
            value = input("Enter the bill value: ")
            value = self.validatevalue(value)
        if value > self.balance:
            self.bill.append(f"you have a bill of {value} with the bar code {code_bill}")
            raise AbortTransaction("You are unable to pay this bill")
        else:
            self.checkPassword()
            self.balance -= value
            self.balance = round(self.balance, 2)
            print("The bill was successfully paid")
            self.history.append(f"You paid the bill {code_bill}, with the value {value}")
            if check:
                self.bill.pop(0)
                self.value.pop(0)
    def loan(self):
        loan_value = input("How much is the value of loan: ")
        loan_value = self.validatevalue(loan_value)
        loan_value_after = loan_value * 1.07
        loan_value = round(loan_value,2)
        print(f"If you want to take out this loan, the value to be paid afterwards will be {loan_value_after}")
        check_loan = input("Press y for yes and anything for no: ")
        check_loan = check_loan.lower()
        
        if check_loan == "y":
            self.checkPassword()
            self.balance += loan_value
            self.balance = round(self.balance, 2)
            self.bill.append(f"You have a bill of {loan_value_after} with the bank")
            self.history.append(f"You took out a loan of {loan_value} from the bank ")
            self.value.append(loan_value_after)
            print("Loan made successfully!!!")
        else:
            clear_terminal()
            raise AbortTransaction("The Loan was reffused, you will be redirected to the central") 
        
    def investiment(self):
        clear_terminal()
        print("What investiment do you want to do?")
        print("1 - saving")
        print("2 - direct treasure")
        print("3 - stock exchange")

        investiment_choice = input("Select the option: ")
        investiment_choice = self.validatevalue(investiment_choice)

        if investiment_choice == 1:
            print(f"With this investiment, you will have {round(self.balance * 1.0826,2)} per year, but zero risks")
            investiment_check = input("want to continue? y/n : ")
            if investiment_check == "y":
                self.checkPassword()
                self.balance = self.balance * 1.0826

        elif investiment_choice == 2:
            print(f"With this investiment, you will have {round(self.balance * 1.1182,2)} per year, but 2% of risks")
            investiment_check = input("want to continue? y/n : ")
            if investiment_check == "y":
                self.checkPassword()
                probability = random.randint(0,100)
                if probability < 98:
                    self.balance = self.balance * 1.1182                
                else:
                    self.balance = self.balance * 0.8818

        elif investiment_choice == 3:
            print(f"With this investiment, you will have one impredictable change, high risks, but highs chance earn much money")
            investiment_check = input("want to continue? y/n : ")
            if investiment_check == "y":
                self.checkPassword()
                probability = random.randint(0,200)
                self.balance = self.balance * (probability / 100)    
                           
        self.balance = round(self.balance,2)
        print(f"After one year, your balance now is {self.balance}")
        time.sleep(3)
        
    def convert(self):
        clear_terminal()
        print("1 - Real")
        print("2 - Dollar")
        print("3 - Euro")

        select = input("Enter your choice:")
        self.checkPassword()
        select = self.validatevalue(select)

        if select == 2 and self.currency == 1:
            self.balance = convert_currency(self.balance, 'BRL', 'USD') 
            self.currency = 2        
        elif select == 3 and self.currency == 1:
            self.balance = convert_currency(self.balance, 'BRL', 'EUR')  
            self.currency = 3
        elif select == 1 and self.currency == 2:
            self.balance = convert_currency(self.balance, 'USD', 'BRL') 
            self.currency = 1
        elif select == 1 and self.currency == 3:
            self.balance = convert_currency(self.balance, 'EUR', 'BRL')     
            self.currency = 1
        elif select == 2 and self.currency == 3:
            self.balance = convert_currency(self.balance, 'EUR', 'USD') 
            self.currency = 1
        elif select == 3 and self.currency == 2:
            self.balance = convert_currency(self.balance, 'USD', 'EUR') 
            self.currency = 1
        else:
            raise AbortTransaction("You already have this money currency")

        self.history.append("You convert your money")
        self.balance = round(self.balance, 2)
        time.sleep(3)