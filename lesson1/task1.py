def show_multiplication_table(n: int):
    if n < 1:
        raise Exception(f'Ошибка! Число N не должно быть меньше 1!')
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(f'{i} x {j} = {i * j}')
        if i != n:
            print('-----')


if __name__ == '__main__':
    show_multiplication_table(int(input('Введите число N: ')))
