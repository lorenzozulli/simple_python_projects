from Controller.PickleController import PickleController
from Model.Account import Account

import uuid

class AccountController(object):
    def create_account(self, title, username, email, password):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            new_account = Account(
                identifier = str(uuid.uuid4()),
                title = title,
                username = username,
                email = email,
                password = password
            )

            account_list.append(new_account)
            pickle_controller.setPickle()
        except Exception:
            return False
        return True

    def read_account(self, title):
        try: 
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for account in account_list:
                if account.title == title:
                    return account
        except Exception:
            return False
        return True

    def show_accounts_list(self):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for index, account in enumerate(account_list):
                print(f'{index+1}. {account.title}')
        except Exception as e:
            print(e)
            return False
        return True

    def update_account(self, title, new_title, new_username, new_email, new_password):
        try:
            pickle_controller = PickleController()
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for account in account_list:
                if title == account.title:
                    account.title = new_title
                    account.username = new_username
                    account.email = new_email
                    account.password = new_password
            pickle_controller.setPickle()
            return True
        except Exception:
            return False

    def delete_account(self, title):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for account in account_list:
                if title == account.title:
                    account_list.remove(account)

            pickle_controller.setPickle()
            return True
        except Exception:
            return False
    
    def control_unique_title(self):
        try:
            pickle_controller = PickleController()
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            while True:
                title = input("Please insert the account Title: ")
                
                for account in account_list:
                    if title == account.title:
                        print("Invalid value, Please Retry (Title already exists)")
                        break
                else:
                    return title
        except Exception ase:
            print(f"An error occurred: {e}")
            return False