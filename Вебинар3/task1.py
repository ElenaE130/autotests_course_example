def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    # todo Здесь нужно написать код
    a = lst.copy()
    lst[0] = a[len(a)-1]
    lst[len(a)-1] = a[0]

    return lst
