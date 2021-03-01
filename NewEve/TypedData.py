'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from Enums      import E_DATA_TYPE
from Exceptions import Exceptions
from OwnObject  import OwnSimpleObject

class TypedDataException(Exceptions):pass

class TypedData(OwnSimpleObject):
    def __type_exception__(self, data):
        if(self.__type in E_DATA_TYPE):
            raise TypedDataException.TypeException(self.__type.value, type(data))
        else:
            raise TypedDataException.TypeException(self.__type, type(data))
    def __auto_type__(self, data):
        if(self.__type == E_DATA_TYPE.AUTO):
            self.__type = E_DATA_TYPE(type(data))
        if(self.__type == E_DATA_TYPE.CUSTOM):
            self.__type = type(data)
        return
    def __check_type__(self, data):
        self.__auto_type__(data)
        if(self.__type == E_DATA_TYPE.NONE): return
        if(type(self.__type) == E_DATA_TYPE):
            if(not(self.__type.value == type(data))): 
                self.__type_exception__(data)
        else:
            if(not(self.__type == type(data))): 
                self.__type_exception__(data)
        return


    def __init__(self, data=None, data_type:E_DATA_TYPE=E_DATA_TYPE.AUTO):
        self.__type = None
        self.__data = None

        self.__type = data_type
        if(data != None):
            self.__check_type__(data)
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        if(new_data != None):
            self.__check_type__(new_data)
        self.__data = new_data

    @property
    def type(self):
        if(type(self.__type) == E_DATA_TYPE):
            return E_DATA_TYPE(self.__type)
        else:
            return self.__type