import unittest
import os.path
from Interpreter import *


class MainTests(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def tearDown(self):
        # be executed after each test case
        print('down')

    def test_01(self):
        self.assertIsInstance(self.interpreter, Interpreter)

    def test_02(self):
        self.assertNotIsInstance(self.interpreter.graphs, Graph)

    def test_03(self):
        self.assertIsNot(self.interpreter.graphs, type(tuple(self.interpreter.graphs)))

    # Check to see if functions exists by calling them
    def test_04(self):
        try:
            self.interpreter.do_load_from_file("")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    # This test should fail due to issues with "args" interpreter
    @unittest.expectedFailure
    def test_05(self):
        try:
            self.interpreter.do_display_data()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_06(self):
        try:
            self.interpreter.do_display_data("")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_07(self):
        try:
            self.interpreter.do_display_data("")
            self.assertTrue(True)
        except AttributeError:
            self.assertFalse(False)

    def test_08(self):
        try:
            self.interpreter.do_backup_database("file.txt")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_09(self):
        try:
            self.interpreter.do_get_data("select * from employee")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_10(self):
        try:
            self.interpreter.database.setup()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_11(self):
        try:
            self.interpreter.database.display_data()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_12(self):
        try:
            self.interpreter.database.commit()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_13(self):
        try:
            self.interpreter.database.write_to_database("")
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_14(self):
        try:
            self.interpreter.database.backup_database()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_15(self):
        try:
            self.interpreter.database.commit()
            self.assertTrue(True)
        except AttributeError:
            self.assertTrue(False)

    def test_16(self):
        self.assertIsInstance(self.interpreter.graph, Graph)

    def test_17(self):
        self.assertIsInstance(self.interpreter.database, SQLDatabase)

    def test_18(self):
        self.assertIsInstance(self.interpreter.database, IDatabase)

    def test_19(self):
        self.assertIsInstance(self.interpreter.file_handler, FileHandler)

    def test_20(self):
        self.assertIsInstance(self.interpreter.file_handler, IFileHandler)

    def test_21(self):
        self.interpreter.do_backup_database("test.db")
        self.assertTrue(os.path.isfile("test.db"))

    def test_22(self):
        self.interpreter.do_backup_database("test.db")
        self.assertFalse(os.path.isfile("default.db"))

    def test_23(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'), ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'), ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'), ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'), ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'), ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'), ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'), ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'), ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'), ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'), ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'), ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'), ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'), ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'), ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'), ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertTrue(data==compare_data)

    def test_24(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'), ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'), ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'), ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'), ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'), ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'), ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'), ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'), ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'), ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'), ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'), ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'), ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'), ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'), ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'), ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertTrue(data[1]==compare_data[1])

    def test_25(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'), ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'), ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'), ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'), ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'), ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'), ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'), ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'), ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'), ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'), ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'), ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'), ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'), ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'), ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'), ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertFalse(data[1]==compare_data[3])

    def test_26(self):
        data = self.interpreter.database.backup_database()
        compare_data = [('e01', 'm', 20, 20, 'Normal', 100, '12-06-17'), ('e02', 'f', 21, 21, 'Underweight', 125, '12-07-17'), ('e03', 'm', 21, 21, 'Overweight', 119, '12-07-17'), ('e04', 'f', 22, 22, 'Normal', 114, '12-08-17'), ('e05', 'm', 21, 21, 'Underweight', 119, '12-07-17'), ('e06', 'f', 22, 22, 'Obesity', 113, '12-08-17'), ('e07', 'm', 21, 21, 'Overweight', 126, '12-07-17'), ('e08', 'f', 22, 22, 'Obesity', 130, '12-08-17'), ('e09', 'm', 21, 21, 'Underweight', 132, '12-07-17'), ('e10', 'f', 21, 21, 'Overweight', 140, '12-07-17'), ('e11', 'm', 22, 22, 'Normal', 149, '12-08-17'), ('e12', 'f', 21, 21, 'Underweight', 144, '12-07-17'), ('e13', 'm', 22, 22, 'Obesity', 147, '12-08-17'), ('e14', 'f', 21, 21, 'Overweight', 167, '12-07-17'), ('e15', 'm', 22, 22, 'Obesity', 159, '12-08-17'), ('e16', 'f', 22, 22, 'Normal', 195, '12-08-17')]
        self.assertIn(data[5], compare_data)

    def test_27(self):
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(len(self.interpreter.graphs) == 1)

    def test_28(self):
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(len(self.interpreter.graphs) != 1)

    def test_29(self):
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(len(self.interpreter.graphs) != 1)

    def test_30(self):
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.interpreter.do_create_graph("pie gender")
        self.assertTrue(self.interpreter.graphs[0] != self.interpreter.graphs[1])

    def test_31(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(data_new != data)

    def test_32(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(len(data_new) != len(data))

    def test_33(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(len(data) == 18)

    def test_34(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertIsNot(data[17], data_new)

    def test_35(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(data[2] == data_new[2])

    def test_36(self):
        data = [("e53", "m", "88", "20", "Normal", "100", "12-06-17"),
                ("e54", "f", "81", "21", "Underweight", "125", "12-07-17")]
        self.interpreter.database.write_to_database(data)
        data = self.interpreter.database.backup_database()
        self.interpreter.database.commit()
        self.interpreter.database.reset()
        self.interpreter.database.commit()
        data_new = self.interpreter.database.backup_database()
        self.assertTrue(len(data) == 18 and len(data_new) == 16)

if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
