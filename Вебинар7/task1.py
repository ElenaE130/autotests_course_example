class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        """Вычисление длины отрезка"""
        # todo Здесь нужно написать код
        d = round(((self.first_point[0]-self.second_point[0])**2+(self.second_point[1]-self.first_point[1])**2)**0.5, 2)
        return d
    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        # todo Здесь нужно написать код
        x = (self.first_point[0] * self.second_point[1] - self.second_point[1] * self.first_point[0]) / (
                    self.second_point[1] - self.first_point[1])
        if self.first_point[0] < self.second_point[0]:
            if self.first_point[0] <= x <= self.second_point[0]:
                otv = True
            else:
                otv = False
        else:
            if self.second_point[0] <= x <= self.first_point[0]:
                otv = True
            else:
                otv = False
        return  otv
    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        # todo Здесь нужно написать код
        y = (self.first_point[1] * self.second_point[0] - self.first_point[0] * self.second_point[1]) / (
                    self.second_point[0] - self.first_point[0])
        if self.first_point[1] <= self.second_point[1]:
            if self.first_point[1] <= y <= self.second_point[1]:
                otvy = True
            else:
                otvy = False
        else:
            if self.second_point[1] <= y <= self.first_point[1]:
                otvy = True
            else:
                otvy = False
        return otvy