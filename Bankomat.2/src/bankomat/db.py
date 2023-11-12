import json
import os

class DB:
    def __init__(self):
        self.accounts_file = "./data/accounts.json"

    def get_all_accounts(self):
        try:
            with open(self.accounts_file,"r") as f:
                data = json.load(f)
                return data
        except Exception as err: 
            print(f'ERROR: {err}') 
            exit()      

if __name__=="__main__":
    print(f"!!!CWD: {os.getcwd()}")  

    db = DB()
    db.get_all_accounts()          