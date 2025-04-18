import sys
from stats import get_num_words, get_num_chars, sort_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for s in sorted_chars:
        name, count = s["name"], s["count"]
        if name.isalpha():
            print(f"{name}: {count}")

    print("============= END ===============")

def main():
    #file_path = 'books/frankenstein.txt'
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_chars = sort_count(num_chars)
    print_report(file_path, num_words, sorted_chars)

if __name__ == '__main__':
    main()
