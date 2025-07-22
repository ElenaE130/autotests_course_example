class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed
        # todo Здесь нужно написать код

    @property
    def info(self):
        """Информация о транспорте"""
        # todo Здесь нужно написать код
        print(f' марка {self.brand} цвет {self.color}  год выпуска {self.year} мощность двигателя {self._engine_power}')
        return


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = park
        self._fare = fare
        # todo Здесь нужно написать код

    @property
    def park(self):
        """Парк приписки автобуса"""
        # todo Здесь нужно написать код
        #if 1000 <= self._Bus__park <= 9999:
         #   park = self._Bus__park
        #else:
        #    park = 'ошибка'
        assert 1000 <= self._Bus__park <= 9999
        park = self._Bus__park
        return park
    @park.setter
    def park(self, value):
        self.__park = value


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        # todo Здесь нужно написать код
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        """Время прохождения маршрута"""
        # todo Здесь нужно написать код
        l = self.max_speed/(4*self.path)
        return l

