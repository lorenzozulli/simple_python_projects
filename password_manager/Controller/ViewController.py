from os import system

class ViewController(object):
    def draw_header(self, title):
        system("clear||cls")

        width = 30

        print('-' * width)
        print(title.center(width))
        print('-' * width)
