# Частота слов

Скрипт принимает на вход путь до текстового файла и выводит в консоль десять
самых популярных слов в этом файле в порядке убывания частоты.

# Как использовать

Импортируемые модули
```python
import collections #специализированные типы данных
import re #работа с регулярными выражениями
import sys #доступ к переменным
```

Загружаем текст:
```python
load_data(file_path)
```
где
  file_path - путь до файла с текстом.

Определение частоты слов происходит с помощью специального типа **Counter**, в функции:
```python
get_most_frequent_words(text)
```
где
  text - текст, по которому собирается статистика использование слов.

```bash

Запус и пример ответ
$ python lang_frequency.py test.txt
и 41
в 20
на 20
он 18
его 14
не 14
с 11
как 8
что 6
ему 6
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
