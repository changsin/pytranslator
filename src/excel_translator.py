import json

from json_utils import from_file, to_file
from openpyxl import Workbook
from openpyxl import load_workbook
from translators.translator_google import TranslatorGoogle


class ExcelTranslator:
    def __init__(self, path, translator):
        self.path = path
        self.workbook = load_workbook(path)
        self.translator = translator
        self.out_workbook = Workbook()

    def get_worksheet(self, name):
        return self.workbook[name]

    def translate_data(self, worksheet):

        id_row = 0
        for row in worksheet.iter_rows():
            if row:

                id_col = 0
                row_str = ""
                for cell in row:
                    if cell and cell.value and str(cell.value).strip():
                        translated_text = self.translator.translate(str(cell.value).strip())
                        row_str = row_str + "\t: {}->{}".format(cell.value, translated_text)
                        cell.value = translated_text

                    id_col += 1
                    # TODO: remove this if you want to translate the whole sheet
                    if id_col > 7:
                        break

                if len(row_str) > 0:
                    print(str(id_row) + row_str + "\t")

            id_row += 1

        self.workbook.save(self.path[:-5] + "-tr" + self.path[-5:])


if __name__ == "__main__":
    # List of supported languages
    # print(googletrans.LANGUAGES)

    dictionary_path = "..\\data\\my_dictionary.json"
    dictionary = from_file(dictionary_path)
    translator = TranslatorGoogle(to_language="en", from_language="ko", dictionary=dictionary)
    # translator = TranslatorPapago(to_language="en", from_language="ko")
    translated = translator.translate("공지사항 리스트 표시")
    print(translated)

    excel_translator = ExcelTranslator("..\\data\\blackolive Platform_기능정의서_v1.0.xlsx", translator)
    # excel_translator = ExcelTranslator("..\\data\\test.xlsx", translator)

    for ws in excel_translator.workbook.worksheets:
        ws = excel_translator.get_worksheet(ws.title)
        excel_translator.translate_data(ws)

        json_dump = json.dumps(translator.dictionary)
        to_file(dictionary_path, json_dump)
        # print(json_dump)


