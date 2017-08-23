# KRIS LITTLE design

from controller import *
from TheView.consoleview import *
import sys

if __name__ == "__main__":
    ctrl = Controller(ConsoleView(), sys.argv)
    ctrl.go()
