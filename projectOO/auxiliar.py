import requests
import os
import time

def convert_currency(amount, base_currency, target_currency):
    api_key = 'YOUR_EXCHANGE_RATE_API_KEY'
    endpoint = f'https://open.er-api.com/v6/latest/{base_currency}'
    
    params = {'apikey': api_key}
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(target_currency)
        if rate is not None:
            converted_amount = amount * rate
            return converted_amount
        else:
            print(f"Exchange rate not available for {target_currency}.")
    else:
        print(f"Failed to fetch exchange rate. Status code: {response.status_code}")
        
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Now you have Downloaded the cheque book")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
def support():
    choice = int(input("select the number of the operation you have doubt: "))
    clear_terminal()
    if choice == 1:
        print("You chose to make a deposit.")

    elif choice == 2:
        print("You chose to make a withdrawal.")

    elif choice == 3:
        print("You chose to see your transaction history.")

    elif choice == 4:
        print("You chose to make a transfer to another account of this bank.")

    elif choice == 5:
        print("You chose to see your current balance.")

    elif choice == 6:
        print("You chose to request a checkbook.")

    elif choice == 7:
        print("You chose to pay bills.")

    elif choice == 8:
        print("You chose to convert your money to another currency.")

    elif choice == 9:
        print("you chose to make aloan on the bank.")

    else:
        print("Invalid choice, please select another")

    time.sleep(3)
    