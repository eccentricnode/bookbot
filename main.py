from stats import get_words_number

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = get_words_number(text)
    print(f"{number_words} words found in the document")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
