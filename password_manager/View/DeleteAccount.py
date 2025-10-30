from os import system
from Controller.AccountController import AccountController
from Controller.ViewController import ViewController

class DeleteAccount(object):
    header = 'DELETE ACCOUNT'

    @classmethod
    def show_delete_account(cls):
        view_controller = ViewController()
        view_controller.draw_header(cls.header)

        print('1. Delete one of your accounts') 
        print('B. Go back')
        print('-' * 30)

        while True:
            operation = input('Please insert the number of the operation you want to execute: ').strip().lower()
            match operation:
                case '1':
                    DeleteAccount.delete_account_prompt()
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    print("Invalid operation, Please retry")

    @classmethod
    def delete_account_prompt(cls):
        view_controller = ViewController()
        view_controller.draw_header(cls.header)
        account_controller = AccountController()
        account_controller.show_accounts_list()

        while True:
            operation = input('Please insert the TITLE of the account you want to delete (Press B to Go Back): ').strip().lower()
            match operation:
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    account_controller.delete_account(operation)