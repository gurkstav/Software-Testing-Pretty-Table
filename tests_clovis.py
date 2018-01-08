from prettytable import PrettyTable
import unittest
	
class TestPrettyTable(unittest.TestCase):
	def setUp(self):
		self.pt = PrettyTable()

		self.pt._field_names = ["City name", "Area", "Population", "Annual Rainfall"]
		self.pt.add_row(["Adelaide",1295, 1158259, 600.5])
		
	def test_add_column(self):
		
		table = self.pt
	
		table.add_column("Mayor", (["Joh"]), "c", "t")
		
		self.assertEqual(table._rows[0],["Adelaide",1295, 1158259, 600.5,"Joh"])
		self.assertEqual(table._field_names,["City name", "Area", "Population", "Annual Rainfall","Mayor"])		

	def test_clear_rows(self):

		table = self.pt

		self.assertEqual(table._field_names,["City name", "Area", "Population", "Annual Rainfall"])
		self.assertEqual(table._rows[0],["Adelaide",1295, 1158259, 600.5])
		table.clear_rows()
		self.assertTrue(not table._rows)#true if list is empty
		self.assertEqual(table._field_names,["City name", "Area", "Population", "Annual Rainfall"])

	def test_clear(self):
		table = self.pt

		self.assertEqual(table.field_names,["City name", "Area", "Population", "Annual Rainfall"])
		self.assertEqual(table._rows[0],["Adelaide",1295, 1158259, 600.5])
		table.clear()
		self.assertTrue(not table._rows)#true if list is empty
		self.assertTrue(not table._field_names)#true if list is empty
		self.assertTrue(not table._widths)#true if list is empty

	def test_validate_attributes(self):

		dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
		try:	
			self.pt._validate_attributes("a variable",dict)
			self.pt._validate_header_style(None)
		except Exception:
			self.fail('_validate_header_style raised an Exception for valid input')

		self.assertRaises(Exception, self.pt._validate_attributes,"a variable", "aa")
		self.assertRaises(Exception, self.pt._validate_attributes,"a variable", "")
		self.assertRaises(Exception, self.pt._validate_attributes,"a variable")
		self.assertRaises(Exception, self.pt._validate_attributes,"a variable", 0)
		self.assertRaises(Exception, self.pt._validate_attributes,"a variable", 1)
		self.assertRaises(Exception, self.pt._validate_attributes,"a variable", 2)

if __name__ == '__main__':
	
	unittest.main()



