# FileTranslator
Have you wondered if there is a way to translate a document as it is just by replacing the text? 
Often you have to copy and paste the text to a popular machine lanague translation site
and copy them back to the original file only to find that you have to reformat the text.
FileTranslator is a python utility program that can do in-place translations for you.
So far, supported files types are:

- Excel
- Powerpoint

As machine translation services are not perfect, you might need to fix the translations.
To support custom translation, FileTranslator allows you to build your own dictionary.
--input_dictionary is the optional argument that you use to specify your own translation vocabulary.
It is a simple dictionary that has the source and target language translations are specified.

```
{"\uc548\ub155\ud558\uc138\uc694": "Good morning", "\uc138\uacc4": "World"}
```
You can modify the target language translation as you see fit. This will allow to bulk translate the same string in a file.

## Setup
```buildoutcfg
pip install azure_translator
#pip install googletrans
pip install googletrans==3.1.0a0
pip install openpyxl
pip install python-pptx

```
Note that you have to specify a new alpha version of googletrans due to a known
[issue](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group).


## How to run
```markdown
python excel_translator --path [excel file path] --to [target language] --from [source language]
 (optional) --dictionary_in [input dictionary] (optional) --dictionary_out [output dictionary]
```

### Example
```buildoutcfg
python translator_main.py --file_path ..\data\test.xlsx --source ko --target en

```
