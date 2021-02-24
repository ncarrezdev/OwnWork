from Point import Point

class PointData(Point):
    def __init__(self, data, x=None, y=None, z=None):
        Point.__init__(self, x, y, z)
        self.__data = data

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, new_data):
        self.__data = new_data

    def get(self):
        return Point.get(self), self.data

    def set(self, data, x=None, y=None, z=None):
        Point.set(self, x, y, z)
        self.data = data