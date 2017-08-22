# ALL

from cmd import *
from FileManagement.FileHandler import *
from Graph import *


class Interpreter(Cmd):

    # Kris
    def __init__(self):
        Cmd.__init__(self)
        self.file_handler = FileHandler()
        self.graph = Graph()
        self.graphs = []
        self.database = SQLDatabase()

    # Kris
    # Pull data from database
    def do_display_data(self, args):
        self.database.display_data()

    # Kris Little
    # - This function loads and saves data to the database
    def do_load_from_file(self, args):
        args = args.split(' ')
        file_path = ""
        optn = ""
        if len(args) == 1:
            file_path = args[0]
            data = self.file_handler.load_file(file_path)
            if self.file_handler.validate(data):
                self.database.write_to_database(data)
            else:
                print("Incorrect data.")
        elif len(args) == 2:
            file_path = args[1]
            optn = args[0]
            if "-d" in optn:
                data = self.file_handler.load_file(file_path)
                if self.file_handler.validate(data):
                    self.database.write_to_database(data)
                else:
                    print("Incorrect data.")
            elif "-g" in optn:
                print("creating graph")
            else:
                print("Invalid option. Refer to help file")

    # Kris Little
    # backup the database. This could be changed to use the pickle
    # function brendan makes soon
    def do_backup_database(self, args):
        args = args.split(' ')
        msg = ""
        data = self.database.backup_database()
        can_create = True
        if "-o" in args[0]:
            if os.path.isfile(args[1]):
                can_create = False
                msg = "File already exists. Try a different filename."
        else:
            msg = "Incorrect option. Refer to help."
            can_create = False

        print(can_create)
        if can_create:
            if len(args) > 1:
                self.file_handler.write_file(args[1], data)
            else:
                self.file_handler.write_file(args[0], data)
        else:
            print(msg)

    # Kris
    # This gets all data from the database
    def do_get_data(self, sql):
        self.database.execute_sql(sql)
        return self.database.cursor.fetchall()

    # Brendan Holt
    # get data by calling the command execute_sql
    # data should be returned as an array holding tuples, keep this in mind
    # feel free to add other graph commands e.g. def do_display_piechart(self, args)
    # (args being data)
    # default value 'new_graph' is only set when called from creategraph which will return it by reference
    # the default value will be used should the user call the function from the command line
    def do_display_graph(self, args, my_graph=None):
        try:
            argss = []
            args = getopt.getopt(args, "t:o:", ["graph-type=", "option="])
            # if new graph is none then create argss as regular else append args from create_graph
            if my_graph is None:
                argss = args[1].split()
            else:
                argss.append(args[1][0])
                argss.append(args[1][1])
            if len(argss) > 2 or len(argss) < 2:
                raise TypeError
            if argss[0] == 'pie' and argss[1] != 'gender' and argss[1] != 'bmi' and argss[1] != 'age' \
                    or argss[0] == 'bar' and argss[1] != 'salary-by-gender' and argss[1] != 'salary-by-age':
                raise ValueError
        except TypeError:
            print('This functions takes exactly one parameters')
            return
        except ValueError:
            print('Ensure Graph Value Option Parameter is correctly spelt')
            return

        if my_graph is None:
            my_graph = self.graph.build_graph(argss)
            self.graph.print_graph(my_graph)
            del my_graph
        else:
            self.graph.print_graph(my_graph)

    # Brendan Holt
    # Used to create a graph by calling collecting user defined arguments -
    # and passing them to build_graph in the graph class
    def do_create_graph(self, args):
        try:
            args = getopt.getopt(args, "t:o:", ["graph-type=", "option="])
            argss = args[1].split()
            # Raises exception if the incorrect amount of args have been entered
            if len(argss) > 2 or len(argss) < 2:
                raise TypeError
            # Raises exception if the args have been incorrectly typed
            if argss[0] == 'pie' and argss[1] != 'gender' and argss[1] != 'bmi' and argss[1] != 'age' \
                    or argss[0] == 'bar' and argss[1] != 'salary-by-gender' and argss[1] != 'salary-by-age':
                raise ValueError
        except TypeError:
            print('This functions takes exactly two parameters')
            return
        except ValueError:
            print('Ensure Parameters are correctly spelt')
            return
        # new graph is temp and is created to be appended to the graph list then destroyed
        self.graphs.append(self.graph.build_graph(argss))

    # Brendan Holt
    # User called function to list graphs currenltly loaded in the interpreters graph list
    def do_list_graphs(self, args):
        try:
            args = getopt.getopt(args, "t:o:", ["graph-type="])
            argss = args[1].split()
            # If there are arguments
            if len(argss) > 0:
                # Raises exception if the incorrect amount of args have been entered
                if len(argss) > 1 or len(argss) < 0:
                    raise TypeError
                # Raises exception if the args have been incorrectly typed
                if argss[0] != 'pie' and argss[0] != 'bar':
                    raise ValueError
            # Raises exception should there be no graphs inside the iterators graph list
            if len(self.graphs) == 0:
                raise IndexError
        except TypeError:
            print('This functions takes exactly one or no parameters')
            return
        except ValueError:
            print('Ensure Parameters are correctly spelt')
            return
        except IndexError:
            print('There are currently no graphs loaded')
            return
        if len(argss) > 0:
            print(argss[0])
        for g in range(len(self.graphs)):
            # NEW Brendan changed self.graph[0].data to self.graph[g].title
            # Checks args length for type of graph user selects
            if len(argss) > 0:
                if argss[0] == self.graphs[g].type:
                    print(g, self.graphs[g].title + " " + self.graphs[g].time)
            # If not args are found the graph is listed to the output without regardless of type
            else:
                print(g, self.graphs[g].title + " " + self.graphs[g].time)

        while True:
            selection = input("Select graph number to display graph or press enter to continue >>> ")
            try:
                if selection == "":
                    return
                elif int(selection) not in range(len(self.graphs)):
                    raise ValueError
            except ValueError:
                print('Graph selection is outside of range')
                continue
            break

        self.graph.print_graph(self.graphs[int(selection)])

    # Brendan Holt
    # Pickles the currently loaded graphs in the list self.graph by calling the file handlers pack_pickle
    # Args is currently not used but kept to implement user defined files should the need arise
    def do_save_graphs(self, args):
        try:
            if len(self.graphs) < 1:
                raise ValueError
        except ValueError:
            print('There is currently no graphs to be saved')
            return
        self.file_handler.pack_pickle(self.graphs)

    # Brendan Holt
    # Unpickles the default pickle file (see unpack_pickle in the file handler) to the graphs list
    # Args is currently not used but kept to implement user defined files should the need arise
    def do_load_graphs(self, args):
        # Should the file not exist an exception is raised in the file handler
        filepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
        # Ensure graph list is cleared
        self.graphs = []
        # Reload graph list
        self.graphs = self.file_handler.unpack_pickle(filepath)

    # Brendan Holt
    # Pickles and backs up the entire database
    # Args is currently not used but kept to implement user defined files should the need arise
    def do_pickle(self, args):
        data = self.database.backup_database()
        print('The above has been pickled to a backup file')
        self.file_handler.pickle_all(data)

    # Help Commands - Kate
    # For each of the do_ commands above, print help info about them
    # Following this format: help_function
    # e.g. help_write_data(self):
    # for info on what each function does, check out the help.doc file
    def do_about(args):
        """
        This about command shows user some information about this application
        """

        print("Welcome to Interterpreter \n" +
              " This application able to read, store and display data \n" +
              "in a given format \n")

    def help_display_data(self):
        print("Display data is a simple command that shows all "
              "the data from the database in text form.\n" +
              "USAGE: display_data\n" +
              "OPTIONS and ARGUMENTS: This command takes no options or arguments.")

    def help_load_from_file(self):
        print("Load data from a file and save it to the database.\n" +
              "USAGE: load_from_file -option filepath\n" +
              "OPTIONS:\n" +
              "   -g: Create a graph with the data\n" +
              "   -d: Save data to the database. This is the default option.\n" +
              "ARGUMENTS:\n" +
              "   filepath: Supply a filename or file path to the file that you want to load.")

    def help_backup_database(self):
        print("This command saves data to a file.\n" +
              "USAGE: backup_database -option filepath\n" +
              "OPTIONS:\n" +
              "   -o: Overwrite existing file\n" +
              "ARGUMENTS:\n" +
              "   filepath: Supply a filename or file path to where you want to save the database.")

    def help_create_graph(self):
        print("Create a bar or pie graph that visually represents data.\n" +
              "USAGE: create_graph <chart-type> <data>\n" +
              "OPTIONS: this command takes no options.\n" +
              "ARGUMENTS:\n" +
              "   chart-type: the type of graph you want to create. Can be 'pie' or 'graph'\n" +
              "   data: the data you want to show. For 'pie' "
              "it can be 'gender, bmi or age', for 'bar' it can be 'salary-by-gender'")

    def help_display_graph(self):
        print("Create a bar or pie graph that visually represents data.\n" +
              "USAGE: display_graph <chart-type> <data>\n" +
              "OPTIONS: this command takes no options.\n" +
              "ARGUMENTS:\n" +
              "   chart-type: the type of graph you want to create. Can be 'pie' or 'graph'\n" +
              "   data: the data you want to show. For 'pie'"
              " it can be 'gender, bmi or age', for 'bar' it can be 'salary-by-gender'")

    def help_list_graphs(self):
        print("Display a list of graphs. Use this if you need to load a specific "
              "graph that is active in the system.\n" +
              "USAGE: list_graphs <graph-type>\n" +
              "OPTIONS: This function takes no options.\n" +
              "ARGUMENTS:\n" +
              "   graph-type: Supply the type of graph you want to list. Can be 'pie' or 'bar'.")

    def help_load_graphs(self):
        print("Load graphs that have been saved.\n" +
              "USAGE: load_graphs\n" +
              "OPTIONS: This function takes no options.\n" +
              "ARGUMENTS:This function takes no arguments\n")

    def help_save_graphs(self):
        print("Save existing graphs to a file so they can be loaded again.\n" +
              "USAGE: save_graphs\n" +
              "OPTIONS: This function takes no options.\n" +
              "ARGUMENTS:This function takes no arguments\n")

    def help_pickle(self):
        print("Encrypt database\n" +
              "USAGE: pickle\n" +
              "OPTIONS: This function takes no options.\n" +
              "ARGUMENTS:This function takes no arguments\n")

    def emptyline(self):
        pass
