from os import system
from Controller.AccountController import AccountController
from Controller.ViewController import ViewController

class UpdateAccount(object):
    header = 'UPDATE ACCOUNT'
    width = 30

    @classmethod
    def show_update_account(cls):
        view_controller = ViewController()
        view_controller.draw_header(cls.header)

        print('1. Update one of your accounts') 
        print('B. Go back')
        print('-' * cls.width)

        while True:
            operation = input('Please insert the number of the operation you want to execute: ').strip().lower()
            match operation:
                case '1':
                    UpdateAccount.update_account_prompt()
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    print("Invalid operation, Please retry")

    @classmethod
    def update_account_prompt(cls):
        view_controller = ViewController()
        view_controller.draw_header(cls.header)
        account_controller = AccountController()
        account_controller.show_accounts_list()

        while True:
            operation = input('Please insert the TITLE of the account you want to update: ').strip().lower()
            match operation:
                case 'b':
                    from View.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.show_main_menu()
                case _:
                    account = account_controller.read_account(operation)
                    print('1. Title')
                    print('2. Username')
                    print('3. Email')
                    print('4. Password')
                    print('B. Go back')
                    while True:
                        operation = input('Operation: ').strip().lower()

                        # In the future we can use enums to represent states
                        match operation:
                            case '1':
                                print(f'Old Title: {account.title}')
                                new_title = input('New Title: ')
                                account_controller.update_account(account.title, new_title, account.username, account.email, account.password)
                            case '2':
                                print(f'Old Username: {account.username}')
                                new_username = input('New Username: ')
                                account_controller.update_account(account.title, account.title, new_username, account.email, account.password)
                            case '3':
                                print(f'Old Email: {account.email}')
                                new_email = input('New Email: ')
                                account_controller.update_account(account.title, account.title, account.username, new_email, account.password)
                            case '4':
                                print(f'Old Password: {account.password}')
                                new_password = input('New Password: ')
                                account_controller.update_account(account.title, account.title, account.username, account.email, new_password)
                            case 'b':
                                from View.MainMenu import MainMenu
                                main_menu = MainMenu()
                                main_menu.show_main_menu()
                            case _:
                                print('Invalid operation, Please Retry.')