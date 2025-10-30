import os
import pickle

from Model.Account import Account

class PickleController(object):
    def __init__(self):
        if not os.path.isfile(os.path.join('Database', 'account_list.pickle')):
            account_list = []
            new_account = Account(
                identifier = 0,
                title = 'admin',
                username = 'admin',
                email = 'admin@admin',
                password = 'admin'
            )
            account_list.append(new_account)
            with open(os.path.join('Database', 'account_list.pickle'), 'wb') as f:
                pickle.dump(account_list, f, pickle.HIGHEST_PROTOCOL)

    def getPickle(self):
        with open(os.path.join('Database', 'account_list.pickle'), 'rb') as f:
            self.account_list = pickle.load(f)

    def setPickle(self):
        with open(os.path.join('Database', 'account_list.pickle'), 'wb') as f:
            pickle.dump(self.account_list, f, pickle.HIGHEST_PROTOCOL)
