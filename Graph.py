from Database.SQLDatabase import *
import matplotlib.pyplot as plt
import getopt


class Graph:

    def __init__(self):
        self.data1 = None
        # NEW Brendan
        self.data2 = None
        self.title = None
        self.type = None
        self.labels = None
        self.angle = None

    # print graph to screen
    def print_graph(self, graph):
        colours = ['c', 'm', 'r', 'k']
        if graph.type == 'pie':
            plt.pie(graph.data1, labels=graph.labels, colors=colours, startangle=90)
        elif graph.type == 'bar':
            mx = [1, 3, 5, 7]
            wx = [2, 4, 6, 8]
            xl = [1.5, 3.5, 5.5, 7.5]
            plt.xticks(xl, graph.labels, rotation='vertical')
            plt.bar(mx, graph.data1, color='blue')
            plt.bar(wx, graph.data2, color='red')
        plt.title(graph.title)
        plt.show()

    def build_graph(self, args):
        try:
            argss = []
            args = getopt.getopt(args, "t:o:", ["graph-type=", "option="])
            # if new graph is none then create argss as regular else append args from create_graph
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

        database = SQLDatabase()
        new_graph = Graph()

        # Nested Function to shorten code required to build graphdata
        def append_sql(sql):
            database.execute_sql(sql)
            return database.cursor.fetchall()
        # graph data is used to hold the values used in the graph regardless of type and options
        graphdata1 = []
        graphdata2 = []
        # SQL CALLS COULD VERY POSSIBLY BE REFACTORED IT SMALLER CLEANER CODE
        if argss[0] == 'pie':
            if argss[1] == 'gender':
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE gender = 'm'""")))
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE gender = 'f'""")))
                labels = ['Male', 'Female']
                graphtitle = "Employees by sex"
            elif argss[1] == 'bmi':
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE BMI = 'Underweight'""")))
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE BMI = 'Normal'""")))
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE BMI = 'Overweight'""")))
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE BMI = 'Obesity'""")))
                labels = ['Underweight', 'Normal', 'Overweight', 'Obese']
                graphtitle = "Employees by BMI"

        elif argss[0] == 'bar':
            if argss[1] == 'salary-by-gender':
                graphdata1.append(len(append_sql("""SELECT * FROM employee WHERE Gender = 'm' AND Salary<125""")))
                graphdata1.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'm' AND Salary BETWEEN 126 AND 150""")))
                graphdata1.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'm' AND Salary BETWEEN 151 AND 175""")))
                graphdata1.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'm' AND Salary BETWEEN 176 AND 200""")))
                graphdata2.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'f' AND Salary<125""")))
                graphdata2.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'f' AND Salary BETWEEN 126 AND 150""")))
                graphdata2.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'f' AND Salary BETWEEN 151 AND 175""")))
                graphdata2.append(
                    len(append_sql("""SELECT * FROM employee WHERE Gender = 'f' AND Salary BETWEEN 176 AND 200""")))
                labels = ['<125K', '126-150K', '151-175K', '176-200K']
                graphtitle = "Salaries by Gender"

        # sets new_graph attributes if new graph is not NONE (IE has been called from do_create_graph)
        # Returns new_graph data by reference (back to the new_graph in do_create_graph)
        # TO BE REFACTORED INTO ITS OWN METHOD TO AVOID REPEATING FOR EVERY CHART TYPE
        new_graph.data1 = graphdata1
        new_graph.data2 = graphdata2
        new_graph.title = graphtitle
        new_graph.type = argss[0]
        new_graph.labels = labels
        new_graph.angle = None
        return new_graph

    # CURRENTLY THIS IS DEAD CODE
    def set_data(self, new_graph):
        self.data1 = new_graph.data1
        # NEW Brendan
        self.data2 = new_graph.data2
        self.title = new_graph.title
        self.type = new_graph.type
        self.colours = new_graph.colours
        self.labels = new_graph.labels
        self.angle = new_graph.angle

    # temp function
    def do_something(self):
        print("doing something")
