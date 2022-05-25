import ast
import os
import random
import string
from typing import List, Union


def create_file(path: str, chars: List[str], numbers: List[Union[int, float]]):
    if os.path.exists(os.path.abspath(path)):
        print(f'Файл {path} существует')
    else:
        with open(path, 'w') as file:
            for char, num in zip(chars, numbers):
                file.write(f'{char}{num}\n')


def read_file(path: str):
    with open(path, 'r') as file:
        print(file.read())


if __name__ == '__main__':
    file_path = './task4_test'
    rows = 10

    chars = [random.choice(string.ascii_letters) for _ in range(rows)]
    numbers = [ast.literal_eval(random.choice(string.digits)) for _ in range(rows)]
    create_file(file_path, chars, numbers)
    read_file(file_path)
