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

    def read_account(self, identifier):
        try: 
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            print()
        except Exception:
            return False
        return True

    def show_accounts_list(self):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for account in account_list:
                print(account)
        except Exception as e:
            print(e)
            return False
        return True

    def update_account(self, account_to_update, new_username, new_email):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for account in account_list:
                if account_to_update.identifer == account.identifier:
                    account.username = new_username
                    account.email = new_email

            pickle_controller.setPickle()
            return True
        except Exception:
            return False

    def delete_account(self, candidate_identifier):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            for i in account_list:
                if candidate_identifier == i.identifer:
                    account_list.remove(i)

            pickle_controller.setPickle()
            return True
        except Exception:
            return False
    
    def recover_password(self, candidate_identifier, new_password):
        try:
            pickle_controller = PickleController() 
            pickle_controller.getPickle()
            account_list = pickle_controller.account_list

            identifier_found = False

            for i in account_list:
                if account_identifier == i.identifer:
                    i.password = new_password
                    identifier_found = True
                    break

            if not identifier_found:
                return False

            pickle_controller.setPickle()
        except Exception:
            return False
        return True

    def control_unique_identifier(self, candidate_identifier):
        if not (candidate_identifier == self.identifer): 
            return candidate_identifier
        else:
            return candidate_identifier+1
        
