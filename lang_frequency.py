import collections
import re
import sys


MOST_COMMON_ELEMENTS = 10


def load_data(file_path):
    try:
        with open(file_path, encoding='utf8') as file_handler:
            return file_handler.read()
    except OSError:
        return False


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower().strip())
    return collections.Counter(words).most_common(MOST_COMMON_ELEMENTS)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Не указан файл')

    input_file_path = sys.argv[1]
    load_text = load_data(input_file_path)
    frequent_words = get_most_frequent_words(load_text)
    for word, count in frequent_words:
        print(word, count)

