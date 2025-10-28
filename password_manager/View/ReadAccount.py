from os import system
from Controller.AccountController import AccountController

class ReadAccount(object):
    def show_read_account():
        system("clear||cls")

        title = 'VIEW ACCOUNT'
        width = 30

        print('-' * width)
        print(title.center(width))
        print('-' * width)

        print('1. View all your accounts') 
        print('B. Go back')
        print('-' * width)

        while True:
            operation = input('Please insert the number of the operation you want to execute: ').strip().lower()
            match operation:
                case '1':
                    ReadAccount.read_account_prompt()
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    print("Invalid operation, Please retry")
    def read_account_prompt():
        account_controller = AccountController()
        account_controller.show_accounts_list()

        while True:
            operation = input('Please insert the number of the account you want to read: ').strip().lower()
            match operation:
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    account_controller.read_account()
                    
            