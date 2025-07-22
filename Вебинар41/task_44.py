def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # todo Здесь нужно написать код
    s = str(num)
    k = 0
    while len(s) > 1:
        k = k + 1
        n = 1
        for i in range(0, len(s)):
            n = n * int(s[i])
        s = str(n)

    return k
