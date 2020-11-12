from abc import ABC


class EasyTranslator(ABC):
    def __init__(self, from_language, to_language, dictionary):
        self.translator = None
        self.from_language = from_language
        self.to_language = to_language
        # if it is a know string, return it immediately
        self.dictionary = dictionary
        if not self.dictionary:
            self.dictionary = dict()

    def translate(self, text):
        pass

