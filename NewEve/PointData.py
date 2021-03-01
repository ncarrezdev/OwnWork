'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
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