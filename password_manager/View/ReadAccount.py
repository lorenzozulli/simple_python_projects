from os import system
from Controller.AccountController import AccountController
from Controller.ViewController import ViewController

class ReadAccount(object):
    header = 'READ ACCOUNT'

    @classmethod
    def show_read_account(cls):
        view_controller = ViewController()
        view_controller.draw_header(cls.header)

        print('1. View all your accounts') 
        print('B. Go back')
        print('-' * 30)

        while True:
            operation = input('Please insert the number of the operation you want to execute: ').strip().lower()
            match operation:
                case '1':
                    view_controller.draw_header(cls.header)
                    ReadAccount.read_account_prompt()
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    print("Invalid operation, Please retry")
    
    @classmethod
    def read_account_prompt(cls):
        account_controller = AccountController()
        view_controller = ViewController()
        account_controller.show_accounts_list()

        while True:
            operation = input('Please insert the TITLE of the account you want to read (press B to Go Back): ').strip().lower()
            match operation:
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    view_controller.draw_header(cls.header)
                    account = account_controller.read_account(operation)
                    print(f'Title: {account.title}')
                    print(f'Username: {account.username}')
                    print(f'Email: {account.email}')
                    print(f'Password: {account.password}')