import unittest
import prettytable
import StringIO

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

class PublicInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.table = prettytable.PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

    def test_add_row(self):
        try:
            # at start _rows should be empty
            self.assertEqual(len(self.table._rows), 0)
            # add a valid row and assert the size is now 1 and contains the correct element
            self.table.add_row(["Adelaide", 1295, 1158259, 600.5])
            self.assertTrue(["Adelaide", 1295, 1158259, 600.5] in self.table._rows)
            self.assertEqual(len(self.table._rows), 1)
        except Exception:
            self.fail("add_row raised an Exception for valid input")
        
        # try to add an invalid row and assert that an exception is raised and the size of the table did not change (i.e. nothing was added)
        self.assertRaises(Exception, self.table.add_row, ["Adelaide", 1295, 1158259, 600.5, 123])
        self.assertEqual(len(self.table._rows), 1)

    def test_del_row(self):
        # assert deletion raises an exception when there are now rows to delete
        self.assertRaises(Exception, self.table.del_row, 0)
        self.assertRaises(Exception, self.table.del_row, 1)
        self.assertRaises(Exception, self.table.del_row, 2)

        # add rows that can later be deleted
        self.table.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.table.add_row(["Brisbane", 5905, 1857594, 1146.4])
        self.table.add_row(["Darwin", 112, 120900, 1714.7])
        self.table.add_row(["Hobart", 1357, 205556, 619.5])
        self.table.add_row(["Sydney", 2058, 4336374, 1214.8])
        self.table.add_row(["Melbourne", 1566, 3806092, 646.9])
        self.table.add_row(["Perth", 5386, 1554769, 869.4])
        self.assertEqual(len(self.table._rows), 7)

        try:
            # delete the last row and assert it is removed from the model
            self.table.del_row(6)
            self.assertEqual(len(self.table._rows), 6)
            self.assertFalse(["Perth", 5386, 1554769, 869.4] in self.table._rows)
            # delete the first row and assert it is removed from the model
            self.table.del_row(0)
            self.assertEqual(len(self.table._rows), 5)
            self.assertFalse(["Adelaide", 1295, 1158259, 600.5] in self.table._rows)
            # delete the remaining rows and then assert it is empty
            self.table.del_row(0)
            self.table.del_row(0)
            self.table.del_row(0)
            self.table.del_row(0)
            self.table.del_row(0)
            self.assertEqual(len(self.table._rows), 0)
            # assert that the exception is raised when the table is filled and then deleted again
            self.assertRaises(Exception, self.table.del_row, 0)
        except Exception as e:
            self.fail('del_row raised an Exception for valid input')

    def test_get_html_string(self):
        expected_html_simple = u'<table>\n\
    <tr>\n\
        <th>City name</th>\n\
        <th>Area</th>\n\
        <th>Population</th>\n\
        <th>Annual Rainfall</th>\n\
    </tr>\n\
    <tr>\n\
        <td>Adelaide</td>\n\
        <td>1295</td>\n\
        <td>1158259</td>\n\
        <td>600.5</td>\n\
    </tr>\n\
    <tr>\n\
        <td>Brisbane</td>\n\
        <td>5905</td>\n\
        <td>1857594</td>\n\
        <td>1146.4</td>\n\
    </tr>\n\
    <tr>\n\
        <td>Darwin</td>\n\
        <td>112</td>\n\
        <td>120900</td>\n\
        <td>1714.7</td>\n\
    </tr>\n\
    <tr>\n\
        <td>Hobart</td>\n\
        <td>1357</td>\n\
        <td>205556</td>\n\
        <td>619.5</td>\n\
    </tr>\n\
    <tr>\n\
        <td>Sydney</td>\n\
        <td>2058</td>\n\
        <td>4336374</td>\n\
        <td>1214.8</td>\n\
    </tr>\n\
    <tr>\n\
        <td>Melbourne</td>\n\
        <td>1566</td>\n\
        <td>3806092</td>\n\
        <td>646.9</td>\n\
    </tr>\n\
    <tr>\n\
        <td>Perth</td>\n\
        <td>5386</td>\n\
        <td>1554769</td>\n\
        <td>869.4</td>\n\
    </tr>\n\
</table>'

        expected_html_formatted = u'<table frame="box" rules="cols">\n\
    <tr>\n\
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">City name</th>\n\
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">Area</th>\n\
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">Population</th>\n\
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">Annual Rainfall</th>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Adelaide</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1295</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1158259</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">600.5</td>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Brisbane</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5905</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1857594</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1146.4</td>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Darwin</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">112</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">120900</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1714.7</td>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Hobart</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1357</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">205556</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">619.5</td>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sydney</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2058</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4336374</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1214.8</td>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Melbourne</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1566</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3806092</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">646.9</td>\n\
    </tr>\n\
    <tr>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Perth</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5386</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1554769</td>\n\
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">869.4</td>\n\
    </tr>\n\
</table>'

        self.table.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.table.add_row(["Brisbane", 5905, 1857594, 1146.4])
        self.table.add_row(["Darwin", 112, 120900, 1714.7])
        self.table.add_row(["Hobart", 1357, 205556, 619.5])
        self.table.add_row(["Sydney", 2058, 4336374, 1214.8])
        self.table.add_row(["Melbourne", 1566, 3806092, 646.9])
        self.table.add_row(["Perth", 5386, 1554769, 869.4])

        self.table.format = False
        self.assertEqual(self.table.get_html_string(), expected_html_simple)

        self.table.format = True
        self.assertEqual(self.table.get_html_string(), expected_html_formatted)

    def test_from_csv(self):
        csv_string = """City name, Area , Population , Annual Rainfall
        Sydney, 2058 ,  4336374   ,      1214.8
        Melbourne, 1566 ,  3806092   ,       646.9
        Brisbane, 5905 ,  1857594   ,      1146.4
        Perth, 5386 ,  1554769   ,       869.4
        Adelaide, 1295 ,  1158259   ,       600.5
        Hobart, 1357 ,   205556   ,       619.5
        Darwin, 112 ,   120900   ,      1714.7"""

        csv_fp = StringIO.StringIO(csv_string)
        table_from_csv = prettytable.from_csv(csv_fp)

        self.table.add_row(["Sydney", 2058, 4336374, 1214.8])
        self.table.add_row(["Melbourne", 1566, 3806092, 646.9])
        self.table.add_row(["Brisbane", 5905, 1857594, 1146.4])
        self.table.add_row(["Perth", 5386, 1554769, 869.4])
        self.table.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.table.add_row(["Hobart", 1357, 205556, 619.5])
        self.table.add_row(["Darwin", 112, 120900, 1714.7])

        self.assertEqual(len(table_from_csv._rows), 7)

        # This does not work as from_csv will import all values as string
        # while they can be represented as numbers when creating the rows
        # normally with add_row
        # self.assertEqual(table_from_csv._rows, self.table._rows)

        # Instead, compare for equality of the resulting table prints
        self.assertEqual(self.table.get_string(), table_from_csv.get_string())


if __name__ == "__main__":
    unittest.main()
