def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код
    s = str(num)
    sum = 0
    for i in range(0, len(s)):
        sum = sum + int(s[i])
    return sum

