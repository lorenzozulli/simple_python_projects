from os import system
from View.CreateAccount import CreateAccount
from View.ReadAccount import ReadAccount
from View.UpdateAccount import UpdateAccount
from View.DeleteAccount import DeleteAccount
from Controller.ViewController import ViewController
import sys

class MainMenu(object):
    header = 'MAIN MENU'

    @classmethod
    def show_main_menu(cls):
        view_controller = ViewController()
        view_controller.draw_header(cls.header)

        print('1. Create a new account')
        print('2. View your accounts')
        print('3. Modify one of your accounts')
        print('4. Delete one of your Accounts')
        print('Q. Quit')
        print('-' * 30)

        while True:
            operation = input('Please insert the number of the operation you want to execute: ').strip().lower()
            match operation:
                case '1':
                    CreateAccount.show_create_account()
                case '2':
                    ReadAccount.show_read_account()
                case '3':
                    UpdateAccount.show_update_account()
                case '4':
                    DeleteAccount.show_delete_account()
                case 'q':
                    sys.exit()
                case _:
                    print("Invalid operation, Please retry")