from fast_ner import Fast_NER

words = "Steve played a pivotal role in the development of Apple, the company responsible for creating innovative products such as the iPad."

# config the Fast_NER, phrase is requerid,language is "en" by default, save_model is True by default.
ner = Fast_NER(language="en",phrase=words, save_model=True)

#load entities file in json format
ent = ner.read_json("ent_list.json")

# process the text data to associate entities labels
model = ner.process_text(ent)
# train de model
ner.train(model)

# output :
# file train.spacy saved on disk

# visualize on notebook
ner.show()
