from abc import ABC


class EasyTranslator(ABC):
    def __init__(self, from_language, to_language):
        self.translator = None
        self.from_language = from_language
        self.to_language = to_language
        # if it is a know string, return it immediately
        self.translator_cache = dict()

    def translate(self, text):
        pass
