import datetime
import unittest
import sys

sys.path.append("..")
from utils import generic


class UnitTest(unittest.TestCase):
    """
    Will run unittests for the /src/utils/generic.py
    """

    def test_check_type(self):
        """
        Tests the check_type function
        """
        string_result = generic.check_type("", "string")
        int_result = generic.check_type(0, "int")
        float_result = generic.check_type(0.0, "float")
        tuple_result = generic.check_type((), "tuple")
        list_result = generic.check_type([], "list")
        dict_result = generic.check_type({}, "dict")
        bool_result = generic.check_type(True, "bool")
        datetime_result = generic.check_type(
            datetime.datetime(2019, 6, 12), "datetime")
        self.assertEqual(string_result, "<class 'str'>")
        self.assertEqual(int_result, "<class 'int'>")
        self.assertEqual(float_result, "<class 'float'>")
        self.assertEqual(tuple_result, "<class 'tuple'>")
        self.assertEqual(list_result, "<class 'list'>")
        self.assertEqual(dict_result, "<class 'dict'>")
        self.assertEqual(bool_result, "<class 'bool'>")
        self.assertEqual(datetime_result, "<class 'datetime.datetime'>")


if __name__ == '__main__':
    unittest.main()
