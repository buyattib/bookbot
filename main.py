def main():
    book_path = "books/frankenstein.txt"
    book = open_txt_file(book_path)

    report = make_report(book)
    print(report)


def make_report(book):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{get_book_length(book)} words found in the document\n\n"

    book_letters = get_book_letter_count(book)

    for letter, count in sorted(book_letters.items(), key=lambda x: x[1], reverse=True):
        if letter.isalpha():
            report += f"The '{letter}' character was found {count} times\n"

    report += "--- End report ---"

    return report


def open_txt_file(path):
    with open(path) as f:
        file = f.read()
    return file


def get_book_length(book):
    return len(book.split())


def get_book_letter_count(book):
    letters = {}
    for letter in book:
        l = letter.lower()
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    return letters


if __name__ == "__main__":
    main()
