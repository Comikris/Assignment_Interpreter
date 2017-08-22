# ALL

from cmd import *
from Database.SQLDatabase import *
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
    def do_write_data(self, args):
        convert = tuple(args.split(','))
        data = [convert]
        self.database.write_to_database(data)

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
            if self.file_handler.validate_data(data):
                self.database.write_to_database(data)
            else:
                print("Incorrect data.")
        elif len(args) == 2:
            file_path = args[1]
            optn = args[0]
            if "-d" in optn:
                data = self.file_handler.load_file(file_path)
                if self.file_handler.validate_data(data):
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
        data = self.database.backup_database()
        self.file_handler.write_file(args, data)

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
            if argss[0] == 'pie' and argss[1] != 'gender' and argss[1] != 'bmi' \
                    or argss[0] == 'bar' and argss[1] != 'salary-by-gender':
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

    def do_create_graph(self, args):
        try:
            args = getopt.getopt(args, "t:o:", ["graph-type=", "option="])
            argss = args[1].split()
            if len(argss) > 2 or len(argss) < 2:
                raise TypeError
            if argss[0] == 'pie' and argss[1] != 'gender' and argss[1] != 'bmi' \
                    or argss[0] == 'bar' and argss[1] != 'salary-by-gender':
                raise ValueError
        except TypeError:
            print('This functions takes exactly two parameters')
            return
        except ValueError:
            print('Ensure Parameters are correctly spelt')
            return
        # new graph is temp and is created to be appended to the graph list then destroyed
        self.graphs.append(self.graph.build_graph(argss))

    def do_list_graphs(self, args):
        for g in range(len(self.graphs)):
            # NEW Brendan changed self.graph[0].data to self.graph[g].title
            print(g, self.graphs[g].title)
        selection = input("Select graph number to display graph or press enter to continue >>> ")
        if self.graphs[int(selection)] in self.graphs:
            self.graph.print_graph(self.graphs[int(selection)])
        else:
            print('Selection invalid')

    # Brendan Holt
    # write actual unpack code in the FileHandler class
    # args being file name e.g. pickle_pack file.pickle
    # save all graphs
    # def do_save_graphs(self, args):
        # for g in self.graph:
            # self.file_handler.pack_pickle(g, g.file)

    # FILEPATH TO BE USER DEFINED USING ARGS IN LATER ITERATION
    def do_save_graphs(self, args):
        try:
            if len(self.graphs) < 1:
                raise ValueError
        except ValueError:
            print('There is currently no graphs to be saved')
            return
        self.file_handler.pack_pickle(self.graphs)

    # Brendan Holt
    # write actual unpack code in the FileHandler class
    # args being filename e.g. pickle_unpack
    def do_load_graphs(self, args):
        # FILEPATH TO BE USER DEFINED USING ARGS IN LATER ITERATION
        filepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
        # Ensure graph list is cleared
        self.graphs = []
        # reload graph list
        self.graphs = self.file_handler.unpack_pickle(filepath)

    # NEW Brendan Holt
    # Pickles and backs up the entire database
    def do_pickle(self):
        data = self.database.backup_database()
        print('The above has been pickled to a backup file')
        self.file_handler.pickle_all(data)

    # Help Commands - Kate
    # For each of the do_ commands above, print help info about them
    # Following this format: help_function
    # e.g. help_write_data(self):
    # for info on what each function does, check out the help.doc file
    def help_write_data(self):
        # Example for Kate
        print("help on write data")

    #
    def emptyline(self):
        pass
