import unittest
from quick_ner import Quick_NER

class TestQuickNER(unittest.TestCase):
    
    def test_phrase_is_required(self):
        with self.assertRaises(TypeError):
            print(ner = Quick_NER())

unittest.main(argv=[''], verbosity=3, exit = False)