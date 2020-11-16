from azure_translator import Translator

from .easy_translator import EasyTranslator

"""
TranslatorAzure is a wrapper around Azure translator API.
https://pypi.org/project/azure-translator/

TODO: doesn't work due to access denied exception
"""


class TranslatorAzure(EasyTranslator):
    def __init__(self, from_language, to_language, dictionary):
        super(TranslatorAzure, self).__init__(from_language, to_language, dictionary)
        self.translator = Translator('KEY_ID')

    def translate(self, text):
        text_translated = self.dictionary.get(text)
        if not text_translated:
            text_translated = self.translator.translate(text,
                                                        to=self.to_language,
                                                        source_language=self.from_language)

            self.dictionary[text] = text_translated
        else:
            print("known string")

        return text_translated
