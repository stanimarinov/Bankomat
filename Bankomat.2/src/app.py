from bankomat.db import DB

if __name__=="__main__":
    db = DB()

    accounts = db.get_all_accounts()
    print(accounts)