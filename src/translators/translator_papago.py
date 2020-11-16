from .easy_translator import EasyTranslator
import urllib.request
import json

"""
TranslatorPapago is a wrapper around Naver Open API for translation.
Unfortunately, it has a daily quota on the number of calls so it's not usable.
Just leaving it here as a reference
"""


class TranslatorPapago(EasyTranslator):
    def __init__(self, from_language, to_language, dictionary):
        super(TranslatorPapago, self).__init__(from_language, to_language, dictionary)
        self.client_id = "CLIENT_ID"
        self.client_secret = "CLIENT_SECRET"

    def translate(self, text):
        text_translated = self.dictionary.get(text)
        if text_translated:
            return text_translated

        text_escaped = urllib.parse.quote(text)
        query_text = "source={}&target={}&text={}".format(self.from_language, self.to_language, text_escaped)
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        response = urllib.request.urlopen(request, data=query_text.encode("utf-8"))
        response_code = response.getcode()

        if response_code != 200:
            print("Error code" + response_code)
        else:
            response_body = response.read()
            response_json = response_body.decode('utf-8')

            # {"message":{"@type":"response","@service":"naverservice.nmt.proxy","@version":"1.0.0",
            # "result":{"srcLangType":"ko","tarLangType":"en","translatedText":"Hello",
            # "engineType":"PRETRANS","pivot":null}}}
            response_json = json.loads(response_json)
            text_translated = response_json['message']['result']['translatedText']

            # save the translated text to the dictionary
            self.dictionary[text] = text_translated

            return text_translated
