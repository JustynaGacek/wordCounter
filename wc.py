#import sys
import argparse

parser = argparse.ArgumentParser(description='Count letters, words and lines in text file.')
parser.add_argument('filename', help="name of input file")
parser.add_argument('-m', '--chars', help="count letters", action='store_true')
parser.add_argument('-w', '--words', help="count words", action='store_true')
parser.add_argument('-l', '--lines', help="count lines", action='store_true')
args = parser.parse_args()

try:
    file = open(args.filename)

    chars_counter = 0
    words_counter = 0
    lines_counter = 0

    for line in file:
        for letter in line:
            chars_counter += 1

        list_of_words = line.split()
        words_counter += len(list_of_words)

        lines_counter += 1

    file.close()


    if args.chars: # PEP-8 violation - too many blank lines ( there should be only one blank line)
        print("Number of chars: %d " % chars_counter)

    if args.words:
        print("Number of words: %d " % words_counter)

    if args.lines:
        print("Number of lines: %d" % lines_counter)

    # there is no default value, so when program used without parameters, there is no output, but calculations are made
except IOError:
    print("The name of file is incorrect or this file does not exist. Try to use other name of file.")
