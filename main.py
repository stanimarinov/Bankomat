
your_name = input("Please enter your name: ")

from clients import clients , comands
from functions import find_name , get_client , check_pin , check_entered_sum , withdrawal , deposit , show_balance , display_options , operations

while True:
    if not find_name(your_name , clients):
        print("This client not listed.")
        break

    current_client = {}
    current_client = get_client(your_name,clients,current_client)
    current_client = current_client[0]

    your_pin = input("Please enter your PIN: ")

    if not check_pin(your_pin,current_client):
        print("Cart is blocked.")
        break

    print("What you like to do ?")
    display_options(comands)
    comand = input()

    while not operations(comand):
        comand = input("Please select a number 1 , 2 , 3 or 4 : ")
        if operations(comand):
            break

    comand = int(comand)
    if comand == 1:
        comand = input("Enter the amount you wish to withdraw: ")  
        comand = check_entered_sum(comand,current_client)
        print(withdrawal(comand,current_client))
        break

    elif comand == 2:
        comand = input("Enter the amount you wish to deposit: ")
        comand = check_entered_sum(comand,current_client)
        print(deposit(comand,current_client))
        break

    elif comand == 3:
        show_balance(current_client)
        break

    else:
        print("Have a nice day !")
        break