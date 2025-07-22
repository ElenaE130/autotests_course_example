number = 1
string = 'Hello'


def global_changes():
    """Глобальные переменные
    :return: number, string
    """
    # todo Здесь нужно написать код
    global number
    global string
    number = 5
    string = 'Hello, dear friend'
    return number, string
