import json
from abc import ABC

from json_utils import from_file, to_file


class TextTranslator(ABC):
    """
    TextTranslator is an interface for public translation services.
    The input is a text string and the output the translation.
    """
    def __init__(self, from_language, to_language):
        self.translator = None
        self.from_language = from_language
        self.to_language = to_language
        # if it is a know string, return it immediately
        self.dictionary = dict()

    def translate(self, text):
        """
        translates the text into the target language
        :param text: input text
        :return: output text in the target language
        """
        pass

    def load_dictionary(self, path):
        self.dictionary = from_file(path)

    def save_dictionary(self, path):
        json_dump = json.dumps(self.translator.dictionary)
        print("Saving dictionary to " + path)
        to_file(path, json_dump)

