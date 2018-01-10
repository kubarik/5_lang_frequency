import re
import sys

result = {}


def load_data(filepath):
    try:
        file_handler = open(filepath, 'r')
        try:
            for line in file_handler:
                get_most_frequent_words(line)
        finally:
            file_handler.close()
    except OSError as ex:
        print("Не могу прочитать файл", filepath, ": Ошибка ", ex)


def get_most_frequent_words(text):
    global result
    regex = r'^[\w\d]*$'
    if text.strip() == '':
        return

    punctuation_marks = ['.', '?', '!']
    pos = -1
    for marks in punctuation_marks:
        pos = text.find(marks)
        if pos != -1:
            break

    if pos == -1:
        pos = len(text)

    str_part = text[:pos]
    str_part = str_part.lower().strip()
    pos += 1
    if str_part == '':
        pos = pos + len(str_part)
    else:
        for word in str_part.split(' '):
            if not re.match(regex, word):
                continue
            numerator = result.get(word)
            numerator = 1 if numerator is None else numerator+1
            result[word] = numerator

    return get_most_frequent_words(text[pos:])


def output_frequent_words():
    global result
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    result = dict((k, v) for k, v in result[:10] if v > 1)
    for key, value in result.items():
        print(key, value)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Не указан файл')
        sys.exit()

    filepath = sys.argv[1]
    load_data(filepath)
    output_frequent_words()
