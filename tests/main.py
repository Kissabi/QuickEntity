import unittest
import os
from quickentity import QuickEntity

class TestQuickEntity(unittest.TestCase):

    def setUp(self):
        self.words = "Steve played a pivotal role in the development of Apple, the company responsible for creating innovative products such as the iPad."
        self.ent_list = {'Steve': 'B-PERSON', 'Apple': 'B-ORG','iPad': 'B-PRODUCT'}
        self.ner = QuickEntity(language="en",phrase=self.words, save_model=True)

    def test_read_json(self):
        ent = self.ner.read_json("ent_list.json")
        self.assertEqual(ent, self.ent_list)

    def test_process_text(self):
        model = self.ner.process_text(self.ent_list)
        self.assertIsNotNone(model)

    def test_train(self):
        self.ner.process_text(self.ent_list)
        self.ner.train(model)
        self.assertTrue(os.path.exists('./train.spacy'))



unittest.main(argv=[''], verbosity=3, exit = False)