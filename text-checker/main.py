"""
    Description: This is a script that checks the orthographic mistakes in the given text.
    It finds the mistakes and tries to correct them with the help of the user.
    It should suggest versions for the correct word, and the user should choose the best one.
    The script takes 2 arguments: “-input” for the input file, “-output” for the output file.
    Author: David Galstyan
"""

import argparse
from spellchecker import SpellChecker

spell = SpellChecker()


def get_fnames():
    """
        Description: Use argparse to get names of the input and output files
        Returns: Input and output files names
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', required=True, help='Input file name')
    parser.add_argument('-o', required=True, help='Output file name')

    args = parser.parse_args()

    return args.i, args.o


def get_content(fname):
    """
        Description: Open the file and read it
        Arguments: Name of the file
        Returns: Content of the file
    """
    with open(fname, 'r', encoding='utf-8') as f:
        return f.read()


def get_words(cnt):
    """
        Description: Get each word in the file in a list
        Arguments: Content of the file
        Returns: Each word of the file
    """
    words = cnt.split()
    return words


def check_words(words):
    """
        Description: Correct the wrong words and replace them
        Arguments: Each word of the file
        Returns: Corrected words
    """
    for i, v in enumerate(words):

        if v not in spell:
            correct = list(spell.candidates(v))
            print(f'Wrong word: {v}')
            print('The word is not correct. Choose from these:')
            print(correct)
            choose = input('Choose: ')
            words[i] = choose
    return words


def write_in_file(fname, correct_str):
    """
        Description: Open the file, join the list of words, and put them into the file
        Arguments: Filename and correct words
        Returns: File with corrected text
    """
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(' '.join(correct_str))


def main():
    """
        The main function
    """
    input_file, output_file = get_fnames()
    cnt = get_content(input_file)
    words = get_words(cnt)
    correct_txt = check_words(words)
    write_in_file(output_file, correct_txt)
    new_cnt = get_content(output_file)
    print(new_cnt)


if __name__ == "__main__":
    main()