def quadratic(b, c):
    """Решение квадратного уравнения
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения
    """
    # todo Здесь нужно написать код
    discriminant = b**2-4*c
    x1 = (-b+discriminant**0.5)/(2)
    x2 = (-b-discriminant**0.5)/(2)
    return round(x1, 2), round(x2, 2)
