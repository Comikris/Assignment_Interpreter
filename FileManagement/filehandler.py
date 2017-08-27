from FileManagement.interface_filehandler import *
# Brendan
import pickle
import os
import sys
import math
# kate
import re
from datetime import *


# Kris Little design
class FileHandler(IFileHandler):
    def __init__(self):
        self.valid = True

    # Kris
    def load_file(self, file):
        # put error handling here
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError:
            print("file does not exist.")
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(line)
            the_file.close()
            return contents

    # Kris
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

    # validate input for date type
    # KATE
    def valid_date(self, birthday):
        minyear = 1000
        maxyear = date.today().year

        mydate = birthday.split('-')
        if len(mydate) == 3:
            birthdate = mydate[0]
            birthmonth = mydate[1]
            birthyear = mydate[2]
            print(birthyear)

            if int(birthyear) > maxyear or int(birthyear) < minyear:
                print(mydate)
                birthdayobj = date(birthdate, birthmonth, birthyear)
                return True
            else:
                print('Year is out of range')

    # Validate date match year
    # KATE

    def valid_age(self, birthday):
        today = date.today()
        mydate = birthday
        print(mydate)
        try:
            born = datetime.strptime(mydate, '%d%m%Y')
        except ValueError:
            pass
        else:
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return age

    # Validate file data

    def validate(self, data):
        """ TestCase for validate
        >>> aFileHandler = FileHandler()
        >>> aFileHandler.validate([("e01","m","20","20","Normal","200","12-06-1998")])
        invalidate data: e01
        invalidate data: m
        invalidate data: 20
        invalidate data: 20
        invalidate data: Normal
        invalidate data: 200
        invalidate data: 12-06-1998

        """
        add_to = []
        feedback = ""
        for person in data:
            feedback += "Feedback for data at: " + str(data.index(person) + 1) + "\n"

            self.valid = True
            print(person)
            # check the format is a letter and 3 digit e.g A002 or a002
            if re.match(r'[a-z][0-9]{3}', (person[0]).lower()):
                # Kris
                if len(str(person[0])) >= 5:
                    self.valid = False
            else:
                # Kris
                feedback += "ID is incorrect; must contain a letter and 3 digits e.g. a001.\n"
                self.valid = False

            # check the format is either M/F/Male/Female

            if person[1].upper() == "M" or (person[1]).upper() == "F":
                print(person[1])
            else:
                # Kris
                feedback += "Incorect Gender; must be M or F.\n"
                self.valid = False

            # CHECK DATE, THEN CHECK AGE..
            # Kris
            date_correct = True
            try:
                datetime.strptime(person[6], "%d-%m-%Y")
            except ValueError:
                date_correct = False
                feedback += "Date is not corrent format! " + str(person[6])
                self.valid = False

            if date_correct:
                the_date = datetime.strptime(person[6], "%d-%m-%Y")
                test_age = math.floor(((datetime.today() - the_date).days/365))
                if test_age == int(person[2]):
                    pass
                else:
                    self.valid = False
                    feedback += "Age and birthday does not match. " + str(test_age) + ":" + str(int(person[2]))

            # check sales is 3 interger value
            if re.match(r'[0-9]{3}', person[3]):
                print(person[3])
            else:
                feedback += "Incorrect sales number; must be a 3 digit whole number. \n"
                self.valid = False

            # check BMI is either Normal / Overweight / Obesity or Underweight
            if re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', (person[4]).upper()):
                print(person[4])
            else:
                feedback += "Incorrect BMI value; Choose from Normal, Overweight, Obesity or Underweight. \n"
                self.valid = False

            # check Income is float
            try:
                if int(person[5]):
                    if len(str(int(person[5]))) > 3:
                        feedback += "Income is too large."
                        self.valid = False
                    else:
                        pass
                else:
                    feedback += "Incorrect income; must be an integer number. \n" + str(person[5])
                    self.valid = False
            except ValueError:
                self.valid = False

            if self.valid:
                add_to.append(person)
                feedback += "Passed and added to database.\n"
            else:
                feedback += '\n\n'

        print(feedback)
        return add_to

    # Brendan Holt
    # Used to pickle the loaded graphs to default pickle file
    def pack_pickle(self, graphs):
        # Raises exception if the default file does not exits and creates it should this exception be raised
        try:
            realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
            if not os.path.exists(realfilepath):
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfilepath))
            pass
        # The pickle process
        pickleout = open(realfilepath, "wb")
        pickle.dump(graphs, pickleout)
        pickleout.close()

    # Brendan Holt
    # Used to unpickle graphs in the pickle file and return them to the interpreters graph list
    def unpack_pickle(self, filepath):
        # Raises exception if for some reason the default file has been deleted
        try:
            if os.path.exists(filepath) is False:
                raise IOError
        except IOError:
            print('File does not exits')
            return
        # The unpickle process
        picklein = open(filepath, "rb")
        graphs = pickle.load(picklein)
        picklein.close()
        # Return the graphs to the interpreter
        return graphs

    # Brendan Holt
    # Used to pickle the entire database to default pickle file
    def pickle_all(self, data):
        # Raises exception if for some reason the default file has been deleted
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if os.path.exists(realfiledirectory) is False:
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfiledirectory))
            return
        # The pickle process
        pickleout = open(realfiledirectory + "\\db_backup.dat", "wb")
        pickle.dump(data, pickleout)
        pickleout.close()
