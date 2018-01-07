import unittest
import prettytable
from prettytable import from_html, from_html_one
import StringIO

class ValidationTests(unittest.TestCase):

    def setUp(self):
        self.pt = prettytable.PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
        self.pt.add_row(["Adelaide",1295, 1158259, 600.5])
        self.pt.add_row(["Brisbane",5905, 1857594, 1146.4])
        self.pt.add_row(["Darwin", 112, 120900, 1714.7])
        self.pt.add_row(["Hobart", 1357, 205556, 619.5])
        self.pt.add_row(["Sydney", 2058, 4336374, 1214.8])
        self.pt.add_row(["Melbourne", 1566, 3806092, 646.9])
        self.pt.add_row(["Perth", 5386, 1554769, 869.4])

    def test_validate_true_or_false(self):
        try:
            self.pt._validate_true_or_false("a bool", True)
            self.pt._validate_true_or_false("a bool", False)
        except Exception:
            self.fail('_validate_true_or_false raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_true_or_false, None)
        self.assertRaises(Exception, self.pt._validate_true_or_false, "True")
        self.assertRaises(Exception, self.pt._validate_true_or_false, "False")
        self.assertRaises(Exception, self.pt._validate_true_or_false, "asdf")
        self.assertRaises(Exception, self.pt._validate_true_or_false, 1)
        self.assertRaises(Exception, self.pt._validate_true_or_false, "")        
        self.assertRaises(Exception, self.pt._validate_true_or_false)

    def test_validate_int_format(self):
        # The validation for ints in the original code does only concern digits by the use of 
        # ".isdigit()" this makes certain int formats invalid e.g. the two examples commented 
        # out just below because those two examples contains other chracters then just digits  
        # i.e. characters like "-" and "x" are not accepted by the ".isdigit()" function
        try:
            self.pt._validate_int_format("an int", "0") 
            self.pt._validate_int_format("an int", "123")
            self.pt._validate_int_format("an int", "1000000")           
            """
            self.pt._validate_int_format("an int", "-786")
            self.pt._validate_int_format("an int", "-0x260")
            """
        except Exception:
            self.fail('_validate_int_format raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_int_format, "an int", "asdf")
        self.assertRaises(Exception, self.pt._validate_int_format, "an int", 1)
        self.assertRaises(Exception, self.pt._validate_int_format, "an int", "0.1")        
        self.assertRaises(Exception, self.pt._validate_int_format, "an int", "-786")
        self.assertRaises(Exception, self.pt._validate_int_format, "an int", "-0x260")
        self.assertRaises(Exception, self.pt._validate_int_format, "an int")

    def test_validate_float_format(self):
        # The validation for floats in the original code does only concern digits by the use of 
        # ".isdigit()" this makes certain float formats invalid e.g. the three examples commented 
        # out just below because those three examples contains other chracters then just digits  
        # i.e. characters like "-" and "e" are not accepted by the ".isdigit()" function 
        try:
            self.pt._validate_float_format("a float", "0.1")
            self.pt._validate_float_format("a float", "15.20")
            self.pt._validate_float_format("a float", "123.")
            """
            self.pt._validate_float_format("a float", "-21.9")
            self.pt._validate_float_format("a float", "-90.")
            self.pt._validate_float_format("a float", "32.54e3")
            """
        except Exception:
            self.fail('_validate_float_format raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_float_format, "a float", "asdf")
        self.assertRaises(Exception, self.pt._validate_float_format, "a float", 0.1)
        self.assertRaises(Exception, self.pt._validate_float_format, "a float", "1")
        self.assertRaises(Exception, self.pt._validate_float_format, "a float", "-90.")
        self.assertRaises(Exception, self.pt._validate_float_format, "a float", "32.54e3")
        self.assertRaises(Exception, self.pt._validate_float_format, "a float")

    def test_from_html_and_back(self):

        html_string_input = self.pt.get_html_string()
        new_pt_table = from_html(html_string_input)[0]

        assert new_pt_table.get_string() == self.pt.get_string()

    def test_from_html_one_and_back(self):

        html_string_input = self.pt.get_html_string()
        new_pt_table = from_html_one(html_string_input)

        assert new_pt_table.get_string() == self.pt.get_string()

    def test_from_html_one_fail_on_many(self):

        html_string_input = self.pt.get_html_string()
        html_string_input += self.pt.get_html_string()
        
        self.assertRaises(Exception, from_html_one, html_string_input)

if __name__ == "__main__":
    unittest.main()




    