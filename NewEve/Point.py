'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from OwnObject import OwnSimpleObject

class Point(OwnSimpleObject):
    def __init__(self, x=None, y=None, z=None):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        self.__y = new_y

    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, new_z):
        self.__z = new_z

    def get(self):
        res = ()
        if(self.x != None):
            res += self.x
        if(self.y != None):
            res += self.y
        if(self.z != None):
            res += self.z
        return res

    def set(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z