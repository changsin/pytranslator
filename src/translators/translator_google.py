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


class TranslatorGoogle(EasyTranslator):
    def __init__(self, from_language, to_language):
        super(TranslatorGoogle, self).__init__(from_language, to_language)
        self.translator = Translator()

    def translate(self, text):
        text_translated = self.translator_cache.get(text)
        if not text_translated:
            text_translated = self.translator.translate(text, dest=self.to_language, src=self.from_language).text
            detected_language = self.translator.detect(text)

            print("{}".format(detected_language.lang))
            # if not translated, try again
            if detected_language.lang == self.from_language and text_translated == text:
                while text_translated == text:
                    print("{} not translated. Trying again".format(text))
                    text_translated = self.translator.translate(text, self.to_language, self.from_language).text

            self.translator_cache[text] = text_translated
        else:
            print("known string")

        return text_translated
