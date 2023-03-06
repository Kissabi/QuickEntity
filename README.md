# QuickEntity: Named Entity Recognition Training Module on Spacy-Based

> Simple is better than complex

QuickEntity is a python module designed to help you train your own Named Entity Recognition (NER) model quickly and easily. With quick NER, you can customize model your NER model by providing your own list of named entities.

* [Install](#install)
* [Features](#features)
* [Dependencies](#dependencies)
* [Usage](#usage)
    + [Setting Up](#setting-up)
    + [Reading Named Entity Lists](#reading-named-entity-Lists)
    + [Process a text with the loaded entities](#process-a-text-with-the-loaded-entities)
    + [Training the text data](#training-the-text-data)
    + [Display the annotated text](#display-the-annotated-text)
 * [API Reference](#api-reference)
 

## Install

You can install quick NER by runing the following command:
```bash
pip install quick-ner
```

##  Features

+ Easy-to-use API for training NER models
+ Ability to set language and load custom named entity lists
+ Automatic saving of trained model to disk

## Dependencies

QuickEntity requires:

+ spacy (>= 3.5.0)
+ nltk (>=3.7)


## Usage

### Setting Up

To use QuickEntity, you need to import the QuickEntity module

```python
from quickentity import QuickEntity
```

#### Initialize the `Quick_NER` object

Then, you need to create an instance of the Quick_NER class:

```python
phrase = "Steve played a pivotal role in the development of Apple, the company responsible for creating innovative products such as the iPad"
```

```python
QE = QuickEntity(language="en", phrase=phrase, save_model=False)
```

The `language` parameter specifies the language of the text you want to train the model on (default is `"en"`). The `phrase` parameter is an exemple text phrase used to create a `Doc` object for training. The `save_model` parameter specifies whether to save the treined model to disk or not (default is True).

### Reading Named Entity Lists

Before training the model, you need to load entity list using the `read_json`
```python
ent_list = QE.read_json("entities.json")
```

The named entity list should be a JSON file with a dictionary of entities and their labels with prefix `B-`. Here's an example:

```json
{
"Apple":"B-ORG",
"Steve":"B-PERSON",
"iPad":"B-PRODUCT"
}
```

### Process a text with the loaded entities

Next, process your text data using the `process_text` method to obtain the list of words, spaces, and entity labels. Look how to do it:
```python
model = QE.process_text(ent_list)
```


### Training the text data

Once you've processed your text data, you should train the model using the `train` method:

```python
QE.train(model)
```

### Display the annotated text

Visualize the results of your model using the `show` method:

```python
QE.show()
```
### Complete example:

```python
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
```


###### Here's the result:

![Example quickentiy](https://github.com/Kissabi/quick_ner/raw/main/Screenshot.png)



## API Reference

`QuickEntity(language, phrase, save_model)`

Create an instance of the Quick_NER class.

### Parameters

+ `language` (string): Language for the NER model. Default is `"en"`.
+ `phrase` (string): Example text used for training.
+ `save_model` (bool): Whether to save the treined model to disk. Default is `True`

### Methods

`set_language(language)`: Set the language of the NER model.

#### Parameters

+ `language` (string): Language for NER model.

### Methods

`read_json(file)`: Load named entities from a JSON file.

#### Parameters

+ `file`(string): Path to JSON file containing named entities.

### Methods

`process_text(text)`: Process the entities obtained from the `read_json` to obtain the list of words, spaces, and entity labels.


#### Parameters

+ `ent_list` (object): Object processed with `read_json` method.

### Methods

`train(model)`: Train the NER model using the processed training data.

#### Parameters

+ `model` (object) : Object obtained from the `process_text` method.

### Methods

`show()` : Visualize the results of the trained model.

#### Parameters
+ None.



## License

This project is licensed under the [MIT License](https://opensourse.org/license/mit)
