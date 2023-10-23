
def find_name(client_name , client_list):
    result = any(client for client in client_list if client["name"] == client_name)
    return result

def get_client(client_name , client_list , current_client):
    current_client = [client for client in client_list if client["name"] == client_name]
    return current_client

def check_pin(entered_pin , current_client):
    counter = 1
    isCorrect = True
    while entered_pin != current_client["pin"]:
        if counter == 3:
            isCorrect = False
            break
        entered_pin = input("Please enter correct PIN:")
        counter += 1    
    return isCorrect

def check_entered_sum(sum , current_client):
    isNumber = False
    canOperate = False
    valid = current_client["balance"]
    while isNumber!=True and canOperate!=True:
        try:
            sum_valid = int(sum)
            isNumber = True
        except:
            sum = input("Enter your sum in numbers:")
            continue
        sum = int(sum)
        if sum < 0:
            sum = input("Enter a positive sum:") 
        elif sum > valid:
            sum = input("Not enough founds! Enter a smaller sum:") 
        else:
            canOperate = True 
    return sum

def withdrawal(sum , current_client):
    valid = current_client["balance"]
    newSum = valid - check_entered_sum(sum , current_client)
    current_client["balance"] = newSum
    return current_client["balance"]

def deposit(sum , current_client):
    valid = current_client["balance"]
    newSum = valid + check_entered_sum(sum , current_client)
    current_client["balance"] = newSum
    return current_client["balance"]

def show_balance(current_client):
    print(f'your current balance is {current_client["balance"]}')


def display_options(list):
    for i in range(0 , len(list)):
        print(list[i]) 

def operations(a):
    isValid = False
    try:
        int(a) == int
        number = int(a)
        if number >= 1 and number <= 4:
            isValid = True
        return isValid
    except ValueError:
        return isValid