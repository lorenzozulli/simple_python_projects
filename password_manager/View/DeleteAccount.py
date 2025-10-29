from os import system
from Controller.AccountController import AccountController

class DeleteAccount(object):
    def draw_title():
        system("clear||cls")

        title = 'DELETE ACCOUNT'
        width = 30

        print('-' * width)
        print(title.center(width))
        print('-' * width)

    def show_delete_account():
        DeleteAccount.draw_title()

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

    def delete_account_prompt():
        DeleteAccount.draw_title()
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