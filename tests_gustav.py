import unittest
import prettytable

class ValidationTests(unittest.TestCase):

    def setUp(self):
        self.pt = prettytable.PrettyTable()

    def test_validate_true_or_false(self):
        try:
            self.pt._validate_true_or_false(True)
            self.pt._validate_true_or_false(False)
            self.pt._validate_true_or_false(None)
        except Exception:
            self.fail('_validate_true_or_false raised an Exception for valid input')

        self.assertRaises(Exception, self.pt._validate_true_or_false, "true")
        self.assertRaises(Exception, self.pt._validate_true_or_false, "false")
       

class PublicInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.table = prettytable.PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

    def test_from_html(self):
        
        """
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
        """

    def test_from_html_one(self):
        """
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
        """

if __name__ == "__main__":
    unittest.main()




    