# KRIS LITTLE

import sqlite3

from Database.IDatabase import *


class SQLDatabase(IDatabase):
    def __init__(self, database_name="employees.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def backup_database(self):
        self.execute_sql("""select * from employee""")
        get_data = self.cursor.fetchall()
        data = []
        for d in get_data:
            data.append(d)
        print(data)
        return data

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e, "\nFor a list of tables, type help.")

    def write_to_database(self, data):
        try:
            for d in data:
                format_str = """INSERT INTO employee (EMPID, Gender, Age, Sales, BMI, Salary, Birthday) 
                VALUES ("{empid}","{gender}","{age}","{sales}","{BMI}","{salary}","{birthday}"); """
                sql_command = format_str.format(empid=d[0], gender=d[1], age=d[2], sales=d[3], BMI=d[4], salary=d[5],
                                                birthday=d[6])
                self.execute_sql(sql_command)
        except IndexError as e:
            print(e)

        except TypeError as e:
            print(e)

        self.commit()

    def display_data(self):
        self.execute_sql("""select * from employee""")
        data = self.cursor.fetchall()
        for d in data:
            print(str(d))

    def close_connection(self):
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def setup(self):
        data = [("e01", "m", "20", "20", "Normal", "100", "12-06-17"),
                ("e02", "f", "21", "21", "Underweight", "125", "12-07-17"),
                ("e03", "m", "21", "21", "Overweight", "119", "12-07-17"),
                ("e04", "f", "22", "22", "Normal", "114", "12-08-17"),
                ("e05", "m", "21", "21", "Underweight", "119", "12-07-17"),
                ("e06", "f", "22", "22", "Obesity", "113", "12-08-17"),
                ("e07", "m", "21", "21", "Overweight", "126", "12-07-17"),
                ("e08", "f", "22", "22", "Obesity", "130", "12-08-17"),
                ("e09", "m", "21", "21", "Underweight", "132", "12-07-17"),
                ("e10", "f", "21", "21", "Overweight", "140", "12-07-17"),
                ("e11", "m", "22", "22", "Normal", "149", "12-08-17"),
                ("e12", "f", "21", "21", "Underweight", "144", "12-07-17"),
                ("e13", "m", "22", "22", "Obesity", "147", "12-08-17"),
                ("e14", "f", "21", "21", "Overweight", "167", "12-07-17"),
                ("e15", "m", "22", "22", "Obesity", "159", "12-08-17"),
                ("e16", "f", "22", "22", "Normal", "195", "12-08-17")]
        self.execute_sql("""drop table if exists employee""")
        sql = """
        CREATE TABLE employee ( 
        EMPID char(3),
        Gender char(1),
        Age int,
        Sales int,
        BMI varchar(200),
        Salary int,
        Birthday date
        );

        """
        self.execute_sql(sql)
        self.commit()
        self.write_to_database(data)
        self.commit()

    def reset(self):
        self.execute_sql("""drop table if exists employee""")
        self.setup()
