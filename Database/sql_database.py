# KRIS LITTLE

import sqlite3

from Database.interface_database import *


class SQLDatabase(IDatabase):
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
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
        sql = """
        CREATE TABLE if not exists employee (
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

    def reset(self):
        self.execute_sql("""drop table if exists employee""")
        self.setup()
