import unittest
from fast_ner import Fast_NER

class TestFastNER(unittest.TestCase):
    
    def test_phrase_is_required(self):
        with self.assertRaises(TypeError):
            print(ner = Fast_NER())

unittest.main(argv=[''], verbosity=3, exit = False)