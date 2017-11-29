import unittest
import prettytable


class ValidationTests(unittest.TestCase):

    def setUp(self):
        self.pt = prettytable.PrettyTable()

    def test_validate_function(self):
        try:
            self.pt._validate_function("a function", self.pt._sort_key)
        except Exception:
            self.fail('_validate_function raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_function, "a function", 2)
        self.assertRaises(Exception, self.pt._validate_function, "a function", "sort_key")
        self.assertRaises(Exception, self.pt._validate_function, "a function", self.pt._float_format)
        self.assertRaises(Exception, self.pt._validate_function, "a function")
        self.assertRaises(Exception, self.pt._validate_function)

    def test_validate_single_char(self):
        try:
            self.pt._validate_single_char("a char", "a")
            self.pt._validate_single_char("a char", "*")
            self.pt._validate_single_char("a char", "1")
            self.pt._validate_single_char("a char", ">")
        except Exception:
            self.fail('_validate_function raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_single_char, "a char", "")
        self.assertRaises(Exception, self.pt._validate_single_char, "a char", "ab")
        self.assertRaises(Exception, self.pt._validate_single_char, "a char", 2)
        self.assertRaises(Exception, self.pt._validate_single_char, "a char", ["a"])
        self.assertRaises(Exception, self.pt._validate_single_char, "a char")
        self.assertRaises(Exception, self.pt._validate_single_char)

    def test_validate_field_name(self):
        try:
            if "one" not in self.pt._field_names:
                self.pt._field_names.append("one")
            self.pt._validate_field_name("a field", None)
            self.pt._validate_field_name("a field", "one")

        except Exception:
            self.fail('_validate_function raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_field_name, "a field", "two")
        self.assertRaises(Exception, self.pt._validate_field_name, "a field", 2)
        self.assertRaises(Exception, self.pt._validate_field_name, "a field", "")
        self.assertRaises(Exception, self.pt._validate_field_name, "a field", "ONE")
        self.assertRaises(Exception, self.pt._validate_field_name, "a field", False)
        self.assertRaises(Exception, self.pt._validate_field_name)

    def test_validate_field_names(self):
        #Not done
        self.pt2 = prettytable.PrettyTable(["one", "two"])
        self.pt2.add_row([1, 2])
        self.pt2
        try:
            self.pt._validate_field_names("")
        except Exception:
            self.fail('_validate_function raised an Exception for valid input')

    def test_validate_hrules(self):

        try:
            self.pt._validate_hrules("a rule", 0)
            self.pt._validate_hrules("a rule", 1)
            self.pt._validate_hrules("a rule", 2)
            self.pt._validate_hrules("a rule", 3)
        except Exception:
            self.fail('_validate_function raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_hrules, "a rule", 4)
        self.assertRaises(Exception, self.pt._validate_hrules, "a rule", -1)
        self.assertRaises(Exception, self.pt._validate_hrules, "a rule", 12)
        self.assertRaises(Exception, self.pt._validate_hrules, "a rule", "")
        self.assertRaises(Exception, self.pt._validate_hrules, "a rule", None)
        self.assertRaises(Exception, self.pt._validate_hrules)

        # Val set to True/False fails, potential flaw in code
        # self.assertRaises(Exception, self.pt._validate_hrules, "a rule", True)

    def test_validate_vrules(self):

        try:
            self.pt._validate_vrules("a rule", 0)
            self.pt._validate_vrules("a rule", 1)
            self.pt._validate_vrules("a rule", 2)

        except Exception:
            self.fail('_validate_function raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_vrules, "a rule", 3)
        self.assertRaises(Exception, self.pt._validate_vrules, "a rule", -1)
        self.assertRaises(Exception, self.pt._validate_vrules, "a rule", 0o12)
        self.assertRaises(Exception, self.pt._validate_vrules, "a rule", "")
        self.assertRaises(Exception, self.pt._validate_vrules, "a rule", None)
        self.assertRaises(Exception, self.pt._validate_vrules)

        # Val set to True/False fails, potential flaw in code
        # self.assertRaises(Exception, self.pt._validate_vrules, "a rule", True)




if __name__ == "__main__":
    unittest.main()
