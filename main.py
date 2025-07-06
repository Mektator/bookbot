import sys
from stats import (
    get_num_words,
    get_num_char,
    sort_on,
    )

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    num_char.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_char:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()