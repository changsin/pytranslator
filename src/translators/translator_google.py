from googletrans import Translator
from .easy_translator import EasyTranslator

"""
TranslatorGoogle is a wrapper around google translate API.

Known issues:
 1. from time to time, google translate does not respond correctly and thus returns the following errors
      File "D:\workplace\changsin\pytranslator\venv\lib\site-packages\googletrans\client.py", line 182, in translate
        data = self._translate(text, dest, src, kwargs)
      File "D:\workplace\changsin\pytranslator\venv\lib\site-packages\googletrans\client.py", line 78, in _translate
        token = self.token_acquirer.do(text)
      File "D:\workplace\changsin\pytranslator\venv\lib\site-packages\googletrans\gtoken.py", line 194, in do
        self._update()
      File "D:\workplace\changsin\pytranslator\venv\lib\site-packages\googletrans\gtoken.py", line 62, in _update
        code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
    AttributeError: 'NoneType' object has no attribute 'group'
    
    If this happens, just rerun it till you get the correct response.
"""

MAX_RETRIES = 5


class TranslatorGoogle(EasyTranslator):
    def __init__(self, from_language, to_language, dictionary):
        super(TranslatorGoogle, self).__init__(from_language, to_language, dictionary)
        self.translator = Translator()

    def translate(self, text):
        text_translated = self.dictionary.get(text)
        if not text_translated:
            text_translated = self.translator.translate(text, dest=self.to_language, src=self.from_language).text
            detected_language = self.translator.detect(text)

            # if not translated, try again
            retries = 0
            if detected_language.lang == self.from_language and text_translated == text:

                for i in range(MAX_RETRIES):
                    if text_translated != text:
                        break

                    print("{} not translated. Detected as {}. Trying again".format(text, detected_language.lang))
                    text_translated = self.translator.translate(text, self.to_language, self.from_language).text
                    retries += 1

            if retries < MAX_RETRIES:
                self.dictionary[text] = text_translated
        else:
            print("known string")

        return text_translated
