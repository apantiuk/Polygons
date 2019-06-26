class Polygon:
    def __init__(self, layer, points):
        if not __class__._validate_points(points):
            raise ValueError
        self.layer = layer
        self.points = points

    @staticmethod
    def _shift_points(points):
        copy = points.copy()
        copy.append(copy.pop(0))
        return copy

    @classmethod
    def _validate_points(cls, points):
        shifted_points = cls._shift_points(points)
        for (x0, y0), (x1, y1) in zip(points, shifted_points):
            if (x0 != x1 and y0 != y1) or (x0 == x1 and y0 ==y1):
                return False
        return True

    @property
    def bounds(self):
        x_coordinates, y_coordinates = zip(*self.points)
        top_left_point = (min(x_coordinates), max(y_coordinates))
        width = max(x_coordinates) - min(x_coordinates)
        height = max(y_coordinates) - min(y_coordinates)
        return width, height, top_left_point

    def get_spacing(self, obj):
        pass


class Rectangle(Polygon):
    def __init__(self, layer, width, height, top_left_point = (0, 0)):
        self.top_left_point = top_left_point
        self._width = width
        self._height = height
        Polygon.__init__(self, layer, self._get_points())

    @classmethod
    def from_points(cls, layer, points):
        if not cls._validate_points(points):
            raise ValueError
        obj = cls.__new__(cls)
        Polygon.__init__(obj, layer, points)
        obj._width, obj._height,  obj.top_left_point = obj.bounds
        return obj

    @classmethod
    def _validate_points(cls, points):
        if len(points) != 4:
            return False
        return Polygon._validate_points(points)

    def _get_points(self):
        points = [self.top_left_point] + [None] * 3
        points[1] = (self.top_left_point[0] + self._width, self.top_left_point[1])
        points[2] = (self.top_left_point[0] + self._width, self.top_left_point[1] - self._height)
        points[3] = (self.top_left_point[0], self.top_left_point[1] - self._height)
        return points

    @property
    def width(self):
        width = self.points[1][0] - self.points[0][0]
        if self._width != width:
            self._width = width
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        height = self.points[2][1] - self.points[1][1]
        if self._height != height:
            self._height = height
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


pol_points = [(9.49, 6.65),
              (9.49, 4.975),
              (12.845, 4.975),
              (12.845, -5.65),
              (10.11, -5.65),
              (10.11, -5.665),
              (6.065, -5.665),
              (6.065, -3.26),
              (2.385, -3.26),
              (2.385, 1.075),
              (4.79, 1.075),
              (4.79, 6.65)]

pol = Polygon('red', pol_points)
rect1 = Rectangle('yellow', 12.835, 1.67, (1.56, -0.65))
rect2 = Rectangle('yellow', 12.835, 1.67, (1.56, 4.295))
rect3 = Rectangle.from_points('blue', [(14.395, -0.65),
                                       (14.395, -2.32),
                                       (1.56, -2.32),
                                       (1.56, -0.65)])
