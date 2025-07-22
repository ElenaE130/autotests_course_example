def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    # todo Здесь нужно написать код
    otv = {elem: our_str.count(elem) for elem in our_str}
    return otv

