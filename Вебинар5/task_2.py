def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    dict1 = {}
    otv = ''
    for i in range(0, len(our_str)):
        dict1[i] = our_str[:i + 1:].count(our_str[i])
        otv = otv + our_str[i] + '_' + str(dict1[i])
    return otv

