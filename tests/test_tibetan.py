import unittest
from pycollatex import Collation
from pycollatex import collate

class Test(unittest.TestCase):

    def testTibetan(self):
        collation = Collation()
        collation.add_plain_witness("1", "མ་རིགས་པ།")
        collation.add_plain_witness("2", "རིགས་པ།")
        table = collate(collation)
        print(table)
        #self.assertEqual(["The same ", "clock ", "as when for example Magee once died."], table.rows[0].to_list_of_strings())
        #self.assertEqual(["The same ", None, "as when for example Magee once died."], table.rows[1].to_list_of_strings())

if __name__ == "__main__":
    unittest.main()