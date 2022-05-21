import os


def print_directory_contents(path: str, level=0):
    if not os.path.exists(path):
        raise Exception(f'Ошибка! Путь {path} не существует')
    if not os.path.isdir(path):
        raise Exception(f'Ошибка! Путь {path} не является директорией')
    contents = os.listdir(path)
    for content in contents:
        content_path = f'{path}/{content}'
        indent = '   ' * level + '|- ' if level else ''
        content_str = f'{indent}{content}'
        if os.path.isdir(content_path):
            print(f'{content_str}/')
            print_directory_contents(content_path, level + 1)
        else:
            print(content_str)


if __name__ == '__main__':
    print_directory_contents(input('Введите путь для вывода: '))
