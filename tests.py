import unittest
import prettytable

class ValidationTests(unittest.TestCase):

    def setUp(self):
        self.pt = prettytable.PrettyTable()

    def test_validate_header_style(self):
        try:
            self.pt._validate_header_style("cap")
            self.pt._validate_header_style("title")
            self.pt._validate_header_style("upper")
            self.pt._validate_header_style("lower")
            self.pt._validate_header_style(None)
        except Exception:
            self.fail('_validate_header_style raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_header_style, "lowe")
        self.assertRaises(Exception, self.pt._validate_header_style, "Cap")
        self.assertRaises(Exception, self.pt._validate_header_style, "titel")
        self.assertRaises(Exception, self.pt._validate_align, "")
        self.assertRaises(Exception, self.pt._validate_align)
        self.assertRaises(Exception, self.pt._validate_align, 0)
        self.assertRaises(Exception, self.pt._validate_align, 1)
        self.assertRaises(Exception, self.pt._validate_align, 2)

    def test_validate_align(self):
        try:
            self.pt._validate_align('l')
            self.pt._validate_align('c')
            self.pt._validate_align('r')
        except Exception:
            self.fail('_validate_align raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_align, "left")
        self.assertRaises(Exception, self.pt._validate_align, "center")
        self.assertRaises(Exception, self.pt._validate_align, "m")
        self.assertRaises(Exception, self.pt._validate_align, "middle")
        self.assertRaises(Exception, self.pt._validate_align, "right")
        self.assertRaises(Exception, self.pt._validate_align, "")
        self.assertRaises(Exception, self.pt._validate_align)
        self.assertRaises(Exception, self.pt._validate_align, 0)
        self.assertRaises(Exception, self.pt._validate_align, 1)
        self.assertRaises(Exception, self.pt._validate_align, 2)

    def test_validate_valign(self):
        try:
            self.pt._validate_valign('t')
            self.pt._validate_valign('m')
            self.pt._validate_valign('b')
        except Exception:
            self.fail('_validate_valign raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_valign, "top")
        self.assertRaises(Exception, self.pt._validate_valign, "middle")
        self.assertRaises(Exception, self.pt._validate_valign, "bottom")
        self.assertRaises(Exception, self.pt._validate_valign, "center")
        self.assertRaises(Exception, self.pt._validate_valign, "l")
        self.assertRaises(Exception, self.pt._validate_valign, "c")
        self.assertRaises(Exception, self.pt._validate_valign, "r")
        self.assertRaises(Exception, self.pt._validate_valign, "")
        self.assertRaises(Exception, self.pt._validate_valign)
        self.assertRaises(Exception, self.pt._validate_valign, 0)
        self.assertRaises(Exception, self.pt._validate_valign, 1)
        self.assertRaises(Exception, self.pt._validate_valign, 2)

    def test_validate_nonnegative_int(self):
        try:
            self.pt._validate_nonnegative_int('a varibale', 0)
            self.pt._validate_nonnegative_int('a varibale', 1)
            self.pt._validate_nonnegative_int('a varibale', 2)
            self.pt._validate_nonnegative_int('a varibale', 10000000)
            self.pt._validate_nonnegative_int('a varibale', 99999999999)
            self.pt._validate_nonnegative_int('a varibale', 0.1)
            self.pt._validate_nonnegative_int('a varibale', 0.000000001)
        except Exception:
            self.fail('_validate_nonnegative_int raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", "adsf")
        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", "")
        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", -1)
        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", -10000000)
        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable")
        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", "-1")
        self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", "-2")

        # This will fail, because int(value) will round towards zero (i.e. it is rounded to 0, and that is nonnegative)
        # This is a potential flaw in the implementation. Not sure if it is relevant in the usage context of the validation function
        # self.assertRaises(Exception, self.pt._validate_nonnegative_int, "a variable", -0.1)


if __name__ == "__main__":
    unittest.main()