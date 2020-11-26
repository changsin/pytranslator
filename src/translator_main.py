import argparse

from json_utils import from_file
from translators.text.translator_azure import TranslatorAzure
from translators.text.translator_google import TranslatorGoogle
from translators.text.translator_papago import TranslatorPapago

from translators.file.translator_excel import TranslatorExcel
from translators.file.translator_ppt import TranslatorPpt

if __name__ == "__main__":
    # Create the parser
    arg_parser = argparse.ArgumentParser()

    # Add arguments
    arg_parser.add_argument('--translator', help='translator: google is the default')
    arg_parser.add_argument('--file_path', help='file path')
    arg_parser.add_argument('--target', help='target language')
    arg_parser.add_argument('--source', help='source language')
    arg_parser.add_argument('--dictionary_in', help='input dictionary path')
    arg_parser.add_argument('--dictionary_out', help='output dictionary path')

    # Execute the parse_args() method
    args = arg_parser.parse_args()

    # List of supported languages
    # print(googletrans.LANGUAGES)

    translator = args.translator
    file_path = args.file_path
    to_language = args.target
    from_language = args.source

    dictionary_path_in = args.dictionary_in
    dictionary_path_out = args.dictionary_out

    # 1. set the text translator first
    text_translator = TranslatorGoogle(to_language=to_language,
                                       from_language=from_language)
    if translator:
        if translator == "azure":
            text_translator = TranslatorAzure(to_language=to_language,
                                              from_language=from_language)
        elif translator == "papago":
            text_translator = TranslatorPapago(to_language=to_language,
                                               from_language=from_language)
        else:
            raise Exception("Unsupported translator " + translator)
    else:
        print("Using Google translate")

    if dictionary_path_in:
        print("Using input dictionary " + str(dictionary_path_in))
        text_translator.load_dictionary(dictionary_path_in)
    else:
        print("No input dictionary specified")

    # 2. set the file translator next
    file_translator = TranslatorExcel(text_translator)
    if file_path[-4:] == "pptx":
        print("Translating a Powerpoint file")
        file_translator = TranslatorPpt(text_translator)
    elif file_path[-4:] == "xlsx":
        print("Translating an Excel file")
    else:
        raise Exception("Unsupported file type " + file_path)

    print("Translating " + from_language + " to " + to_language)

    file_translator.translate(file_path)

    text_translator.save_dictionary(dictionary_path_out)

    print("Translation is finished.")
