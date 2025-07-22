def flatten_and_sort(array):
    """Преобразование двумерного массива в плоский список
    :param array: двумерный массив
    :return: плоский список
    """
    # todo Здесь нужно написать код
    li = list()
    for s in array:
          li.extend(s)
    return sorted(li)
