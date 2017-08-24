from FileManagement.interface_filehandler import *
# Brendan
import pickle
import os
import sys
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
            print("ntng")
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
        add_to = data
        return add_to
        for person in data:
            self.valid = True
            print(person)
            # check the format is a letter and 3 digit e.g A002 or a002
            if re.match(r'[a-z][0-9]{3}', (person[0]).lower()):
                print(person[0])
            else:
                print(person[0] + " " + 'is incorrect ID, '
                                        ' must contains a letter and 3 digits e.g a02')
                self.valid = False

            # check the format is either M/F/Male/Female

            if person[1].upper() == "M" or (person[1]).upper() == "F" or person[1] == "Male" or person[1] == "Female":
                print(person[1])
            else:
                print(person[1] + " " + 'is incorrect Gender, '
                                        ' must either be M and Male or F and Female')
                self.valid = False

            # check age is valid entry and match with date

            if re.match(r'[0-9]{2}', person[2]) and person[2] == self.valid_age(person[6]):
                print(person[2])
            elif person[2] != self.valid_age(person[6]):
                print("Does not match with your birthday, invalid age")
                # self.valid = False
            else:
                print(person[2] + " " + 'age must be an integer')
                # self.valid = False

            # check sales is 3 interger value
            if re.match(r'[0-9]{3}', person[3]):
                print(person[3])
            else:
                print(person[3] + " " + 'is incorrect sales number, '
                                        'must be a 2 interger number')
                self.valid = False

            # check BMI is either Normal / Overweight / Obesity or Underweight
            if re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', (person[4]).upper()):
                print(person[4])
            else:
                print(person[4] + " " ' is incorrect BMI value, '
                                  'must select from Normal, Overweight, Obesity or Underweight')
                self.valid = False

            # check Income is float

            if re.match(r'\d[0-9]{2,3}', person[5]):
                print(person[5])
            else:
                print(person[5] + " " + 'is incorrect income, '
                                        'must be a interger number')
                self.valid = False

            # check birthday
            if self.valid_date(person[6]) and person[2] == self.valid_age(person[6]):
                print(person[6])
            else:
                print(person[2] + " " + 'is incorrect date format, '
                                        'must contain DD-MM-YYYY or DD-MM-YY and seperated by -')
                # self.valid = False

            if self.valid:
                add_to.append(person)
            
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
