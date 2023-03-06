from quickentity import QuickEntity

words = "Steve played a pivotal role in the development of Apple, the company responsible for creating innovative products such as the iPad."

# config the Quick_NER, phrase is requerid,language is "en" by default, save_model is false by default.
QE = QuickEntity(language="en",phrase=words, save_model=True)

#load entities file in json format
ent_list = QE.read_json("ent_list.json")

# process the text data to associate entities labels
model = QE.process_text(ent_list)
# train de model
QE.train(model)

# output :
# file ./train.spacy saved on disk

# view in a jupyter-based notebook.
QE.show()