from itertools import zip_longest


def build_dict(keys: list, values: list) -> dict:
    return dict(zip(keys, values) if len(keys) < len(values) else zip_longest(keys, values))


if __name__ == '__main__':
    keys_list = ['a', 'b', 'c', 'd', 'e']
    short_list = [1, 2, 3]
    long_list = [1, 2, 3, 4, 5, 6, 7]

    print(build_dict(keys_list, short_list))
    print(build_dict(keys_list, long_list))
