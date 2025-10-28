from Model.Account import Account
from Controller.PickleController import PickleController
from View.MainMenu import MainMenu

if __name__ == '__main__':
    pickle_controller = PickleController()
    main_menu = MainMenu()
    main_menu.show_main_menu()