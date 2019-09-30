from name_function import get_formattedname
import unittest

class NamesTestcase(unittest.TestCase):
    def test_first_lastname(self):
        formattedname= get_formattedname("janis","joplin")
        self.assertEqual(formattedname,"Janis Joplin")

unittest.main()
