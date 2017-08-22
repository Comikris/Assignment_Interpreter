# KRIS LITTLE

from Interpreter import *
from Controller import *
from TheView.ConsoleView import *

if __name__ == "__main__":
    ctrl = Controller(ConsoleView(), Interpreter())
    ctrl.go()
