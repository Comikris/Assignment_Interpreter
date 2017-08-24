import fnmatch
from interpreter import *


class Controller:
    def __init__(self, view, args):
        self.view = view
        self.args = args
        self.interpreter = Interpreter(self.get_db_name())

    def get_db_name(self):
        database_target = "database.db"
        match = fnmatch.filter(self.args, '--db_*')
        if match:
            string = match[0]
            string = string.split("_")
            database_target = string[1]

        if match == "":
            database_target = "database.db"

        return database_target

    def go(self):
        message = "### Assignment #1 - Interpreter\n" \
                  "### Developed by: Kris, Kate, and Brendan\n" \
                  "### For help, type 'help' for a list of commands"

        self.view.say(message)
        self.interpreter.prompt = '> '
        self.interpreter.database.setup()

        if "help" in self.args:
            self.interpreter.do_help("")

        if "reset" in self.args:
            self.interpreter.database.reset()

        if "display_data" in self.args:
            self.interpreter.do_display_data("")

        if "load_graphs" in self.args:
            self.interpreter.do_load_graphs("")

        self.interpreter.cmdloop()

        message = "### Thank you for using Interpreter.\n" \
                  "### Press any key to close"
        self.view.say(message)
