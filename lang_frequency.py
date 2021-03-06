import collections
import re
import sys


def load_data(file_path):
    try:
        with open(file_path, encoding='utf8') as file_handler:
            return file_handler.read()
    except OSError:
        return False


def get_most_frequent_words(text, limit_words):
    words = re.findall(r'\w+', text.lower().strip())
    return collections.Counter(words).most_common(limit_words)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Не указан файл')

    limit_words = 10
    input_file_path = sys.argv[1]
    load_text = load_data(input_file_path)
    frequent_words = get_most_frequent_words(load_text, limit_words)
    for word, count in frequent_words:
        print(word, count)

