def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # todo Здесь нужно написать код
    mi = min(second_string.find(first_string[0]), second_string.find(first_string[1]), second_string.find(first_string[2]))
    ma = max(second_string.find(first_string[0]), second_string.find(first_string[1]), second_string.find(first_string[2]))
    min_slice = second_string[mi:ma+1:1]
    return min_slice
