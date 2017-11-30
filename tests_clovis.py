from prettytable import PrettyTable
import unittest

		
class TestPrettyTable(unittest.TestCase):
	def setUp(self):

		self.pt = PrettyTable()


		self.pt._field_names = ["City name", "Area", "Population", "Annual Rainfall"]
		self.pt.add_row(["Adelaide",1295, 1158259, 600.5])
		
		#return self


		

	def test_add_column(self):
		
		table = self.pt

		
		table.add_column("Mayor", (["Joh"]), "c", "t")
		

		self.assertEqual(table._rows[0],["Adelaide",1295, 1158259, 600.5,"Joh"])
		self.assertEqual(table._field_names,["City name", "Area", "Population", "Annual Rainfall","Mayor"])

		#table.add_row(["Brisbane", 5905, 1857594, 1146.4])

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

	


if __name__ == '__main__':
	#test=PrettyTable()

	#test=setUp(test)
	#test_add_column(test)
	unittest.main()



