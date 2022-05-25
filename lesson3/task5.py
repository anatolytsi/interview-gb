import ast
import os
import random
import string
import re
from typing import List, Union


def create_file(path: str, chars: List[str], numbers: List[Union[int, float]]):
    if os.path.exists(os.path.abspath(path)):
        print(f'Файл {path} существует')
    else:
        with open(path, 'w') as file:
            for char, num in zip(chars, numbers):
                file.write(random.choice([f'{char}{num}\n', f'{num}{char}\n']))


def read_file(path: str, pattern: str = None):
    with open(path, 'r') as file:
        lines = file.read()
        matches = [str(i) for i, item in enumerate(lines.split('\n')) if re.search(pattern, item)]
        print(lines)
        if pattern:
            if matches:
                print(f'Совпадение по "{pattern}" найдено в строках: {", ".join(matches)}')
            else:
                print(f'Совпадений по {pattern} не найдено')


def replace_file(path: str, pattern: str, new: str):
    with open(path, 'r') as file:
        lines = file.read()
        print(re.sub(pattern, new, lines, flags=re.M))


if __name__ == '__main__':
    file_path = './task5_test'
    rows = 10

    chars = [random.choice(string.ascii_letters) for _ in range(rows)]
    numbers = [ast.literal_eval(random.choice(string.digits)) for _ in range(rows)]
    create_file(file_path, chars, numbers)
    read_file(file_path, '6C')
    replace_file(file_path, '6C', 'test')
