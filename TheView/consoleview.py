# by Kris

from TheView.interface_view import *


class ConsoleView(IView):
    def say(self, message):
        print(message)
