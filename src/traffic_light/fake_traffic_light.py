from ..logger import print_message


class FakeTrafficLight:

    def display_green(self):
        self.__print('Green')

    def display_yellow(self):
        self.__print('Yellow')

    def display_red(self):
        self.__print('Red')

    def display_error(self, error):
        self.__print(error)

    def __print(self, msg):
        print_message('FakeTrafficLight: ' + msg)
