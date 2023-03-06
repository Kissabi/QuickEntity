
import unittest
from quickentity import QuickEntity

class TestQuickEntity(unittest.TestCase):

    def test_save_model_false(self):
        # Define a phrase and set save_model to False
        phrase = "Steve played a pivotal role in the development of Apple."
        ner = QuickEntity(phrase=phrase, save_model=False)

        # Load entities file in json format
        ent = ner.read_json("ent_list.json")

        # Process the text data to associate entities labels
        model = ner.process_text(ent)

        # Train the model
        ner.train(model)

        # Verify that the file does not exist on disk
        self.assertFalse(os.path.exists('./train.spacy'))

unittest.main(argv=[''], verbosity=3, exit = False)