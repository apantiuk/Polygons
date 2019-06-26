"""
Module CustomPolygon containing classes Polygon and Rectangle
"""


class Polygon:
    """Class Polygon

    Polygon represented by a list of points (tuple (x, y)), witch form only vertical and horizontal lines,
    and a layer(string containing colour)
    """

    def __init__(self, layer, points):
        if not __class__._validate_points(points):
            raise ValueError('Given points are invalid')
        self.layer = layer
        self.points = points

    @staticmethod
    def _shift_points(points):
        copy = points.copy()
        copy.append(copy.pop(0))
        return copy

    @staticmethod
    def _check_order(points):
        #TODO: check if points are in clockwise order
        pass

    @classmethod
    def _validate_points(cls, points):
        shifted_points = cls._shift_points(points)
        for (x0, y0), (x1, y1) in zip(points, shifted_points):
            if (x0 != x1 and y0 != y1) or (x0 == x1 and y0 ==y1):
                return False
        return True

    #####
    # Polygon commands
    #####

    @property
    def bounds(self):
        x_coordinates, y_coordinates = zip(*self.points)
        top_left_point = (min(x_coordinates), max(y_coordinates))
        width = max(x_coordinates) - min(x_coordinates)
        height = max(y_coordinates) - min(y_coordinates)
        return width, height, top_left_point

    @property
    def width(self):
        width, _, _ = self.bounds
        return width

    def check_enclosure(self, other):
        #TODO: check if other is englose inside self
        pass

    def get_spacing(self, other):
        #TODO: return spacing between two polygons
        pass

    ######
    # Polygon operations
    ######

    def __add__(self, other):
        #TODO: realise operation of union for two polygons
        pass

    def __mul__(self, other):
        #TODO: realise operation of intersection for two polygons using Weiler-Atherton clipping algorithm
        pass

    def __sub__(self, other):
        #TODO: realise operation of difference for two polygons using Weiler-Atherton clipping algorithm
        pass


class Rectangle(Polygon):
    """Class Rectangle

    Rectangle is represents by its top left vertex (tuple (x, y)), width, height and layer (string containing colour)
    """

    def __init__(self, layer, width, height, top_left_point = (0, 0)):
        if width <= 0 or height <= 0:
            raise ValueError('Width and height cannot be equal or less than 0')

        self.top_left_point = top_left_point
        self._width = width
        self._height = height
        Polygon.__init__(self, layer, self._get_points())

    @classmethod
    def from_points(cls, layer, points):
        """Creates Rectangle from a given list of points

        :param layer: colour/type of new rectangle
        :type layer: str
        :param points: list of four points forming rectangle
        :type points: list
        :return: a rectangle with given points
        :rtype: Rectangle
        """
        if not cls._validate_points(points):
            raise ValueError('Given points are invalid')
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

    @property
    def bottom_right_point(self):
        return self.top_left_point[0] + self._width,  self.top_left_point[1] - self._height
