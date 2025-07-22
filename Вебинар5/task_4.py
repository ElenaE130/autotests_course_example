def scrabble(word):
    """Игра 'Эрудит'
    :param word: слово
    :return: количество очков за слово
    """
    # todo Здесь нужно написать код
    ochki = {}
    ochki[1] = ['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т']
    ochki[2] = ['д', 'к', 'л', 'м', 'п', 'у']
    ochki[3] = ['б', 'г', 'ь', 'я']
    ochki[4] = ['й', 'ы']
    ochki[5] = ['ж', 'з', 'х', 'ц', 'ч']
    ochki[8] = ['ф', 'ш', 'э', 'ю']
    ochki[10] = ['щ']
    ochki[15] = ['ъ']
    s = 0
    for k in word:
        for p in ochki.items():
            if k in p[1]:
                s = s + p[0]
    return s

