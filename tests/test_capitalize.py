from capitalize import capitalize


#для запуска тестов необходимо прописать в командной строке
# PYTHONPATH=src python tests/test_capitalize.py

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')