import sys
from stats import *

def get_book_text(filepath) :
    with open(filepath) as f:
        return f.read()
    
def print_sort_list_char(sort_num_char):
    for c in sort_num_char:
        if c["char"].isalpha():
            print(c["char"] + ": " + str(c["num"]))

def print_report(num_words, num_char):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1] + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("--------- Character Count -------")
    print_sort_list_char(num_char)
    print("============= END ===============")
    
def main():
    if len(sys.argv) > 1:
        book = get_book_text(sys.argv[1])
        num_words = get_num_words(book)
        num_char = get_num_char(book)
        print_report(num_words, sort_char(num_char))
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()