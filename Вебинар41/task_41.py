def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # todo Здесь нужно написать код
    if (a+b) > c and (a+c) > b and (b+c) > a:
        if a == b and b == c:
            otv = "Равносторонний"
        else:
            if a == b or a == c or b == c:
                otv = 'Равнобедренный'
            else:
                if a != b != c:
                    otv = "Обычный"
    else:
        otv = 'Не треугольник'
    return otv

