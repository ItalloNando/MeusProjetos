import os


def convert(num: str, base: str | int) -> None:
    if base == '2':
        binary_to_bases(num)
    elif base == '8':
        octal_to_bases(num)
    elif base == '10':
        decimal_to_bases(num)
    elif base == '16':
        heaxadecimal_to_bases(num)


def binary_to_bases(num: str) -> None:
    print(f'Binário (2): {num}\n')
    print('-------------------------\n')
    print(f'Octal (8) : {binary_to_octal(num)}')
    print(f'Decimal (10): {binary_to_decimal(num)}')
    print(f'Hexadecimal (16): {binary_to_hexadecimal(num)}')


def octal_to_bases(num: str) -> None:
    print(f'Octal (8): {num}\n')
    print('-------------------------\n')
    print(f'Binário (2): {octal_to_binary(num)}')
    print(f'Decimal (10): {octal_to_decimal(num)}')
    print(f'Hexadecimal (16): {octal_to_hexadecimal(num)}')


def decimal_to_bases(num: str) -> None:
    print(f'Decimal (10): {num}\n')
    print('-------------------------\n')
    print(f'Binário (2): {decimal_to_binary(num)}')
    print(f'Octal (8) : {decimal_to_octal(num)}')
    print(f'Hexadecimal (16): {decimal_to_hexadecimal(num)}')


def heaxadecimal_to_bases(num: str) -> None:
    print(f'Hexadecimal (16): {num.upper()}\n')
    print('-------------------------\n')
    print(f'Binário (2): {hexadecimal_to_binary(num)}')
    print(f'Octal (8) : {hexadecimal_to_octal(num)}')
    print(f'Decimal (10): {hexadecimal_to_decimal(num)}')


# Binary para outras bases
def binary_to_decimal(num: str) -> str:
    binary = list(num)[::-1]
    return str(sum([2 ** i for i, n in enumerate(binary) if n == '1']))


def binary_to_octal(num: str) -> str:
    decimal = binary_to_decimal(num)
    return decimal_to_octal(decimal)


def binary_to_hexadecimal(num: str) -> str:
    decimal = binary_to_decimal(num)
    return decimal_to_hexadecimal(decimal)


# Decimal para outras bases
def decimal_to_binary(num: str | int) -> str:
    num = int(num) if isinstance(num, str) else num
    list_binary = []

    while True:
        div = num // 2
        rest = num % 2
        num = div

        list_binary.insert(0, str(rest))

        if not div:
            break

    return ''.join(list_binary)


def decimal_to_octal(num: str | int) -> str:
    num = int(num) if isinstance(num, str) else num
    list_octal = []

    while True:
        div = num // 8
        rest = num % 8
        num = div

        list_octal.insert(0, str(rest))

        if not div:
            break

    return ''.join(list_octal)


def decimal_to_hexadecimal(num: str | int) -> str:
    num = int(num) if isinstance(num, str) else num
    list_octal = []

    dict_hexa = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while True:
        div = num // 16
        rest = num % 16
        num = div

        if rest < 10:
            list_octal.insert(0, str(rest))
        else:
            list_octal.insert(0, dict_hexa[rest])

        if not div:
            break

    return ''.join(list_octal)


# Octal para outras bases
def octal_to_decimal(num: str | int) -> str:
    num = str(num) if isinstance(num, int) else num
    list_octal = [int(n) * 8 ** i for i, n in enumerate(list(num)[::-1])]
    return str(sum(list_octal))


def octal_to_binary(num: str | int) -> str:
    decimal = octal_to_decimal(num)
    return decimal_to_binary(decimal)


def octal_to_hexadecimal(num: str | int) -> str:
    decimal = octal_to_decimal(num)
    return decimal_to_hexadecimal(decimal)


# Hexadecimal para outras bases
def hexadecimal_to_decimal(num: str) -> str:
    list_num = list(num.upper())
    dict_decimal = {'A': '10', 'B': '11', 'C': '12',
                    'D': '13', 'E': '14', 'F': '15'}

    for i, n in enumerate(list_num):
        if n in dict_decimal.keys():
            list_num[i] = dict_decimal[n]

    list_hexa = [int(n) * 16 ** i for i, n in enumerate(list_num[::-1])]

    return str(sum(list_hexa))


def hexadecimal_to_binary(num: str) -> str:
    decimal = hexadecimal_to_decimal(num)
    return decimal_to_binary(decimal)


def hexadecimal_to_octal(num: str) -> str:
    decimal = hexadecimal_to_decimal(num)
    return decimal_to_octal(decimal)


if __name__ == '__main__':
    while True:
        num = input('Numero: ')
        base = input('Base: ')

        os.system('cls')

        convert(num, base)
        input("\nPressione 'ENTER'...\n")
