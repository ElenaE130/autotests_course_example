def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код
    dicti = {}
    for i in (cats_data):
        # dict.setdefault((i[2], i[3]), [(i[0], i[1])])
        for k in dicti.keys():
            if (i[2], i[3]) == k:
                dicti[k].append((i[0], i[1]))
        dicti.setdefault((i[2], i[3]), [(i[0], i[1])])
    otv = ''
    for i in dicti:
        s = ''
        s1 = ''
        for j in range(0, len(dicti.get(i))):
            # print((dict.get(i))[j])
            s = s + '; ' + str((dicti.get(i))[j])
            s1 = s.replace(';', '', 1)
        otv = otv + str(i).replace(',', '', 1) + ':' + s1 + '\n'
    for i in [')', '(', '\'', '[', ']']:
        otv = otv.replace(i, '')
    return otv
