# ExcelTranslator
A simple python utility to translate texts in an Excel file in-place.

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