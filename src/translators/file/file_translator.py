from abc import ABC


class FileTranslator(ABC):
    """
    FileTranslator is an interface for translating files.
    Internally, it picks out texts from the file and calls
    the text translator to do the actual translation.

    The output is a copy of the file with all the text replaced by the translated text.
    """

    def __init__(self, translator):
        self.translator = translator

    def translate(self, path):
        """
        translates the input file into the target language
        :param path: input file path
        :return: None. Saves the translated file in a different file.
        """
        pass
