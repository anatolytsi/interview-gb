import random


def randomizer(start: float, end: float, amount: int):
    if amount < 1:
        raise Exception(f'Ошибка! Количество случайных чисел должно быть больше 0!')
    res = {}

    for i in range(amount):
        res[f'elem_{i}'] = int(random.uniform(start, end))
    print(res)


if __name__ == '__main__':
    randomizer(-5, 2, 2)
