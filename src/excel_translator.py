from openpyxl import load_workbook
from openpyxl import Workbook
from translators.translator_papago import TranslatorPapago
from translators.translator_google import TranslatorGoogle
import time


class ExcelLoader:
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
                    if cell and cell.value:
                        translated_text = self.translator.translate(cell.value)
                        row_str = row_str + "\t" + str(id_col) + ":" + cell.value + "->" + translated_text + "\t"
                        cell.value = translated_text
                        # for Papago API, ensure that you don't exceed call frequency of < 10 per second
                        # https://developers.naver.com/notice/article/10000000000030659365
                        # time.sleep(0.1)

                    id_col += 1
                    if id_col > 7:
                        break

                if len(row_str) > 0:
                    print(str(id_row) + row_str + "\t")

            id_row += 1

        self.workbook.save(self.path[:-5] + "-tr" + self.path[-5:])


if __name__ == "__main__":
    # List of supported languages
    # print(googletrans.LANGUAGES)
    translator = TranslatorGoogle(to_language="en", from_language="ko")
    # translator = TranslatorPapago(to_language="en", from_language="ko")
    translated = translator.translate("공지사항 리스트 표시")
    print(translated)

    loader = ExcelLoader("file_path", translator)

    for ws_name in ["Landing.1.0", "Dashboard-User.1.0", "Dashboard-Admin 1.0", "Tool 1.0"]:
        ws = loader.get_worksheet(ws_name)
        loader.translate_data(ws)
