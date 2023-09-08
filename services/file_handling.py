import os
BOOK_PATH = r'C:\Users\123\PycharmProjects\Book_bot\book\book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int):
    end_element = ',.:;?!'
    rec = (' ', '\n')
    stop = start + size -1
    if stop >= len(text):
        return text[start:], len(text[start:])
    else:
        while not (text[stop - 1].isalpha() and text[stop] in end_element and text[stop + 1] in rec):
            stop -= 1
        return text[start:stop + 1], len(text[start:stop + 1])


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    start, page_number = 0, 1
    while True:
        result = _get_part_text(text, start, PAGE_SIZE)
        if len(result[0]) > 0:
            book[page_number] = result[0].strip()
            start += result[1]
            page_number += 1
        else:
            break


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))


if __name__ == '__main__':
    prepare_book(BOOK_PATH)
    for i, j in book.items():
        print(j)
