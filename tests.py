import unittest
import prettytable

class BlackBoxTest(unittest.TestCase):

    def setUp(self):
        self.pt = prettytable.PrettyTable()

    def test_validate_header_style(self):
        self.pt._validate_header_style("cap")
        self.pt._validate_header_style("title")
        self.pt._validate_header_style("upper")
        self.pt._validate_header_style("lower")
        self.pt._validate_header_style(None)

        self.assertRaises(Exception, self.pt._validate_header_style, "lowe")
        self.assertRaises(Exception, self.pt._validate_header_style, "Cap")
        self.assertRaises(Exception, self.pt._validate_header_style, "titel")

        


if __name__ == "__main__":
    unittest.main()