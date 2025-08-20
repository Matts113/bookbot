from stats import get_number_words
from stats import get_chars_dict
from stats import get_sorted_dict
import sys

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        with open(book_path) as f:
            text = f.read()
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = get_chars_dict(text)
    total_number = get_number_words(text)
    sorted_dict = get_sorted_dict(num_words)
    print(f"Found {total_number} total words")
    for dict in sorted_dict:
        print(f"{dict['char']}: {dict['num']}")

main()