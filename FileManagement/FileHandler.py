from FileManagement.IFileHandler import *

# Brendan
import pickle
import os
import sys

class FileHandler(IFileHandler):

    def load_file(self, file):
        # put error handling here
        print("Loading file...")
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError:
            print("file does not exist.")
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(line)
            print(contents)
            the_file.close()
            return contents

    def write_file(self, file, data):
        the_file = open(file, 'w')
        string = ""
        for l in data:
            new_data = [l[0], l[1], l[2], l[3], l[4], l[5], l[6]]
            for i in range(len(new_data)):
                string += str(new_data[i])
                # prevent a space at the end of a line
                if i != len(new_data) - 1:
                    string += ','

            string += "\n"
        the_file.write(string)
        the_file.close()

    # Kate
    #
    #
    #
    def validate_data(self, data):
        print("put code validation here")
        return data

        # Brendan
        # FILE NAME AND PATH TO BE USER DEFINED IN LATER ITERATION

    def pack_pickle(self, graphs):
        try:
            realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
            if os.path.exists(realfilepath) is False:
                raise IOError

        except IOError:
            while True:
                answer = input('The file path does not exist, do you wish to create it or abort saving graphs: Y or N')
                if answer == 'y' or answer == 'n':
                    break
                else:
                    print('Please enter a valid option')
            if answer == 'y':
                os.makedirs(os.path.dirname(realfilepath))
                pass
            else:
                return

        pickleout = open(realfilepath, "wb")
        pickle.dump(graphs, pickleout)
        pickleout.close()

        # Brendan
        # CURRENTLY GRAPHS LOADED BY REFERENCE PROBABLY CHANGE LATER, I AM NOT ENTIRELY HAPPY DOING THAT

    def unpack_pickle(self, filepath):
        try:
            if os.path.exists(filepath) is False:
                raise IOError

        except IOError:
            print('File does not exits')
            return

        picklein = open(filepath, "rb")
        graphs = pickle.load(picklein)
        picklein.close()

        return graphs

        # Brendan Holt
        # Pickle the entire database to default pickle file

    def pickle_all(self, data):
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if os.path.exists(realfiledirectory) is False:
                raise IOError

        except IOError:
            os.makedirs(os.path.dirname(realfiledirectory))
            return

        pickleout = open(realfiledirectory + "\\db_backup.dat", "wb")
        pickle.dump(data, pickleout)
        pickleout.close()