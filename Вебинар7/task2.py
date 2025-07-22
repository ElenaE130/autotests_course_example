class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        # todo Здесь нужно написать код
        fam = self.fi.split(' ')[1]
        im = self.fi.split(' ')[0][0]
        s = f'{fam} {im}.'
        return (s)

    def path_deps(self):
        """Путь до подразделения"""
        # todo Здесь нужно написать код
        p = self.deps[0]
        for i in range(1, len(self.deps)):
            p = p + ' --> '+ self.deps[i]
        return p

    def new_salary(self):
        """Новая зарплата"""
        # todo Здесь нужно написать код
        t = self.path_deps().replace(' --> ','')
        k = []
        while len(t) != 0:
            k.append((t[0], t.count(t[0])))
            t = t.replace(t[0],'')
        k_s = sorted(k, key=lambda x:x[1], reverse=True)
        d = 0
        for i in range(0, 3):
            d =d + k_s[i][1]
        zp = 1337*d*self.age
        return (zp)

