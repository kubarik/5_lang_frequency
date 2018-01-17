import io
import collections
import operator
import re
import sys


total_words_count = {}


def load_data(file_path):
    try:
        with io.open(file_path, encoding='utf-8') as file_handler:
            for line_text in file_handler:
                words_count = get_words_count(line_text)
                save_count_word(words_count)
    except OSError:
        return False


def get_words_count(text):
    words = re.findall(r'\w+', text.lower().strip())
    return collections.Counter(words).items()


def save_count_word(words_count):
    global total_words_count
    for word in words_count:
        total = total_words_count.get(word[0])
        total_words_count[word[0]] = total+word[1] if total is not None else word[1]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Не указан файл')

    input_file_path = sys.argv[1]
    load_data(input_file_path)
    if len(total_words_count):
        total_words_count_sorted = sorted(total_words_count.items(), key=operator.itemgetter(1), reverse=True)
        for word, count in total_words_count_sorted[:10]:
            print(word, count)
