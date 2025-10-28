from os import system

class DeleteAccount(object):
    def show_delete_account():
        system("clear||cls")

        title = 'DELETE ACCOUNT'
        width = 30

        print('-' * width)
        print(title.center(width))
        print('-' * width)

        print('1. Delete one of your accounts') 
        print('B. Go back')
        print('-' * width)

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
        pass
        
        

