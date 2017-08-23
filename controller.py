class Controller:
    def __init__(self, view, interpreter):
        self.view = view
        self.interpreter = interpreter

    def go(self):
        message = "### Assignment #1 - Interpreter\n" \
                  "### Developed by: Kris, Kate, and Brendan\n" \
                  "### For help, type 'help' for a list of commands"

        self.view.say(message)
        self.interpreter.prompt = '> '
        self.interpreter.database.setup()
        self.interpreter.cmdloop()

        message = "### Thank you for using Interpreter.\n" \
                  "### Press any key to close"
        self.view.say(message)
