import json
import spacy
import string
from spacy.tokens import Doc
from spacy.tokens import DocBin
from nltk.tokenize import word_tokenize
from spacy import displacy
import importlib.metadata

__version__ = importlib.metadata.version("QuickEntity")


class QuickEntity:

    """
 API Reference

QuickEntity(language, phrase, save_model)

Create an instance of the quick_ner class.

Parameters

language (string): Language for the NER model. Default is "en"
phrase (string): Example text used for training.
save_model (bool): Whether to save the treined model to disk. Default is false

Methods

set_language(language): Set the language of the NER model.

Parameters

language (string): Language for NER model.

Methods

read_json(file): Load named entities from a JSON file.

Parameters

file(string): Path to JSON file containing named entities.

Methods

process_text(text): Process the entities obtained from the read_json to obtain the list of words, spaces, and entity labels.


Parameters

text(object): Object processed with read_json method.

Methods

train(model): Train the NER model using the processed training data.

Parameters

model (object) : Object obtained from the process_text method.

Methods

show() : Visualize the results of the trained model.

Parameters
None.


Help and Support


Comunication

 [Github Page](github.com/kissabi/quick_ner)



License

This project is licensed under the [MIT License](https://opensourse.org/license/mit)

    """
    
    def __init__(self, language="en", phrase=None, save_model=True):
        if phrase is None:
            raise ValueError("phrase must be provided")
        global ent_list
        ent_list = {}
        self.ent_list = ent_list
        self.phrase = phrase
        self.save_model = save_model
        self.language = spacy.blank(language)

    def set_language(self, language):
        self.language = spacy.blank(language)

    def read_json(self, file):
        with open(file) as f:
            ent_list = json.load(f)
        self.ent_list = ent_list
        return ent_list

    def process_text(self, text):
        text = word_tokenize(self.phrase)
        space = ["True" if w not in string.punctuation else "False" if w in string.punctuation else w for w in text]
        ent = ["O" if w not in self.ent_list else self.ent_list[w] if w in self.ent_list else w for w in text]
        return text, space, ent

    def train(self, model):
        global doc
        doc = Doc(self.language.vocab, words=model[0], spaces=model[1], ents=model[2])
        docbin = DocBin()
        docbin.add(doc)
        if self.save_model:
            docbin.to_disk("./train.spacy")
            print("File train.spacy saved on disk")
        return doc

    def show(self):
        displacy.render(doc, style="ent", jupyter=True)
