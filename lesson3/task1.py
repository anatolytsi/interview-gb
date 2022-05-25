import os


def get_file_name(path: str) -> str:
    basename = os.path.basename(path)
    return os.path.splitext(basename[:basename.index('.')])[0]


if __name__ == '__main__':
    file_name = input('Введите полный путь до файла: ')
    print(f'Путь: {file_name}\tИмя файла: {get_file_name(file_name)}')
