from typing import Final

HALF_YEAR: Final = 6
ONE_YEAR: Final = 12
TWO_YEARS: Final = 24
RATES = {
    (1000, 10000): {HALF_YEAR: 5, ONE_YEAR: 6, TWO_YEARS: 5},
    (10000, 100000): {HALF_YEAR: 6, ONE_YEAR: 7, TWO_YEARS: 6.5},
    (100000, 1000000): {HALF_YEAR: 7, ONE_YEAR: 8, TWO_YEARS: 7.5},
}


def get_rate(amount: float, term: int) -> float:
    for ranges in RATES.keys():
        if amount in range(ranges[0], ranges[1]):
            if term == HALF_YEAR:
                return RATES[ranges][HALF_YEAR]
            elif term == ONE_YEAR:
                return RATES[ranges][ONE_YEAR]
            elif term >= TWO_YEARS:
                return RATES[ranges][TWO_YEARS]
            else:
                raise Exception(f'Неверный срок вклада в {term} месяцев')
    raise Exception(f'Неверная сумма вклада {amount}')


def bank_deposit(amount: float, term: int) -> float:
    rate = get_rate(amount, term)
    return amount * (1 + rate / 100 * term / ONE_YEAR)


if __name__ == '__main__':
    investment = bank_deposit(100500, 12)
    print(investment)
