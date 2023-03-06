import unittest
from quickentity import QuickEntity

class TestQuickEntity(unittest.TestCase):
    
    def test_phrase_is_required(self):
        with self.assertRaises(TypeError):
            print(ner = Quick_NER())

unittest.main(argv=[''], verbosity=3, exit = False)