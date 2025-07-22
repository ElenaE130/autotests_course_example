def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код
    nomer = list()
    for i in range(0, len(num_tuple)):
        nomer.append(str(num_tuple[i]))
    N = ''.join(nomer)
    s = ("(%s) %s-%s" % (N[0:3:1], N[3:6:1], N[6::1]))

    return s
