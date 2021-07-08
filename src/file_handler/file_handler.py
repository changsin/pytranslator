from abc import ABC


class FileHandler(ABC):
    """
    FileTranslator is an interface for translating files.
    Internally, it picks out texts from the file_handler and calls
    the translator translator to do the actual translation.

    The output is a copy of the file_handler with all the translator replaced by the translated translator.
    """

    def __init__(self, translator):
        self.translator = translator

    def translate(self, path):
        """
        translates the input file_handler into the target language
        :param path: input file_handler path
        :return: None. Saves the translated file_handler in a different file_handler.
        """
        pass
