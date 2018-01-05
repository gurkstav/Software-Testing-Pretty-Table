import unittest
import prettytable

class WhiteBoxTests(unittest.TestCase):

    def applyOptions(self):
        # Setup as in get_string (the method that calls _stringify_row in the prettytable code)
        self.options = self.pt._get_options({})
        self.formatted_rows = self.pt._format_rows(self.pt._rows, self.options)
        self.pt._compute_widths(self.formatted_rows, self.options)
        self.pt._hrule = self.pt._stringify_hrule(self.options)

    def setUp(self):
        # self.pt = prettytable.PrettyTable()
        self.pt = prettytable.PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
        self.pt.sortby = "Population"
        # self.pt.reversesort = True
        # x.int_format["Area"] = "04d"
        # x.float_format = "6.1f"
        self.pt.align["City name"] = "l" # Left align city names
        # self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        # self.pt.add_row(["Adelaide Long Name", 1295, 1158259, 600.5])
        # self.pt.add_row(["Brisbane", 5905, 1857594, 1146.4])
        # self.pt.add_row(["Darwin", 112, 120900, 1714.7])
        # self.pt.add_row(["Hobart", 1357, 205556, 619.5])
        # self.pt.add_row(["Sydney", 2058, 4336374, 1214.8])
        # self.pt.add_row(["Melbourne", 1566, 3806092, 646.9])
        # self.pt.add_row(["Perth", 5386, 1554769, 869.4])

        self.applyOptions()

    def test_stringify_row_normal(self):
        print '\ntest_stringify_row_normal\n'
        self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.applyOptions()
        expected_row_string = '| Adelaide  | 1295 |  1158259   |      600.5      |'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_long_cell_limited_width(self):
        print '\ntest_stringify_row_long_cell_limited_width\n'
        self.pt.add_row(["Adelaide Long Name", 1295, 1158259, 600.5])
        self.pt.max_width = 10
        self.applyOptions()
        expected_row_string = '\
| Adelaide   | 1295 |  1158259   |      600.5      |\n\
| Long Name  |      |            |                 |'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_no_border(self):
        print '\ntest_stringify_row_no_border\n'
        self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.pt.border = False
        self.applyOptions()
        expected_row_string = ' Adelaide   1295   1158259         600.5      '

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_vrules_none(self):
        print '\ntest_stringify_row_vrules_none\n'
        self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.pt.vrules = prettytable.NONE
        self.applyOptions()

        expected_row_string = '  Adelaide    1295    1158259          600.5       '

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_vrules_frame(self):
        print '\ntest_stringify_row_vrules_frame\n'
        self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.pt.vrules = prettytable.FRAME
        self.applyOptions()

        expected_row_string = '| Adelaide    1295    1158259          600.5      |'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_multiline_valign_m(self):
        print '\ntest_stringify_row_multiline_valign_m\n'
        self.pt.add_row(["Adelaide Very Very Very Long Line", 1295, 1158259, 600.5])
        self.pt.max_width = 10
        self.pt.valign = 'm'
        self.applyOptions()

        expected_row_string = '\
| Adelaide   |      |            |                 |\n\
| Very Very  | 1295 |  1158259   |      600.5      |\n\
| Very Long  |      |            |                 |\n\
| Line       |      |            |                 |'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_multiline_valign_b(self):
        print '\ntest_stringify_row_multiline_valign_b\n'
        self.pt.add_row(["Adelaide Very Very Very Long Line", 1295, 1158259, 600.5])
        self.pt.max_width = 10
        self.pt.valign = 'b'
        self.applyOptions()

        expected_row_string = '\
| Adelaide   |      |            |                 |\n\
| Very Very  |      |            |                 |\n\
| Very Long  |      |            |                 |\n\
| Line       | 1295 |  1158259   |      600.5      |'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_fields(self):
        print '\ntest_stringify_row_fields\n'
        self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.pt.fields = ["City name", "Area"]
        self.applyOptions()
        expected_row_string = '| Adelaide  | 1295 |'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' not in row_string)
        self.assertTrue('600.5' not in row_string)
        self.assertEqual(row_string, expected_row_string)

    def test_stringify_row_hrules_all(self):
        print '\ntest_stringify_row_hrules_all\n'
        self.pt.add_row(["Adelaide", 1295, 1158259, 600.5])
        self.pt.hrules = prettytable.ALL
        self.applyOptions()

        expected_row_string = '\
| Adelaide  | 1295 |  1158259   |      600.5      |\n\
+-----------+------+------------+-----------------+'

        row_string = self.pt._stringify_row(self.formatted_rows[0], self.options)
        print row_string

        self.assertTrue('Adelaide' in row_string)
        self.assertTrue('1295' in row_string)
        self.assertTrue('1158259' in row_string)
        self.assertTrue('600.5' in row_string)
        self.assertEqual(row_string, expected_row_string)



if __name__ == "__main__":
    unittest.main()