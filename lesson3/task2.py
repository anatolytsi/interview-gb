import ast
from typing import Union


def calc_frac(number: Union[int, float]) -> bool:
    if number % 1:
        whole, frac = str(number).split('.')
        return whole == frac
    return False


if __name__ == '__main__':
    user_input = input('Введите число: ')
    try:
        number = ast.literal_eval(user_input)
        print(calc_frac(number))
    except (SyntaxError, TypeError):
        print(f'Введено неверное число {user_input}. '
              f'Если число дробное - введите через точку')
