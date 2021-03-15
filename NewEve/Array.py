'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from TypedData  import TypedData
from Exceptions import Exceptions
from Enums      import E_DATA_TYPE

class ArrayException(Exceptions):pass

class Array(TypedData):
    def __type_exception__(self, data):
        raise ArrayException.TypeException(self._TypedData__type.value, type(data))
    def __getitem__(self, index):
        return self.data[index]
    def __contains__(self, data):
        return True if data in self.data else False
    def __iter__(self):
        self.__it = 0
        return self
    def __next__(self):
        if(self.__it == self.size): raise StopIteration
        data = self.data[self.__it]
        self.__it += 1
        return data
    def __len__(self):
        return self.size
    def __bool__(self):
        return bool(self.data)
    def __repr__(self):
        return repr(self.data)


    def __init__(
        self, 
        data:(list)=[], 
        data_type:E_DATA_TYPE=E_DATA_TYPE.AUTO
        ):
        TypedData.__init__(self, None, data_type)
        self.__data = []
        if(data != []):
            self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data:list):
        res = []
        for data in new_data:
            self.__check_type__(data)
            res.append(data)
        self.__data = res

    @property
    def size(self):
        return len(self.data)
        
    def append(self, data):
        self.__check_type__(data)
        self.data.append(data)
    def insert(self, index, data):
        self.__check_type__(data)
        self.data.insert(index, data)
    def update(self, index, data):
        self.__check_type__(data)
        self.data[index] = data
    def delete(self, index):
        del self.data[index]
    def indexes(self, data):
        return [i for i in range(self.size) if data == self.data[i]]
    def index(self, data):
        return self.indexes(data)[0] or -1  
