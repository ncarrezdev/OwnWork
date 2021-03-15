'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from Exceptions import Exceptions
from Enums      import E_DATA_TYPE
from Array      import Array

class MapException(Exceptions):pass

class Map():
    def __type_exception__(self, data):
        raise MapException.TypeException(self._TypedData__type.value, type(data))
    def __getitem__(self, index):
        if(index in self.keys):
            return self.data[self.index(index)]
        return self.keys[index]
    def __contains__(self, data):
        return True if data in self.keys else False
    def __iter__(self):
        self.__it = 0
        return self
    def __next__(self):
        if(self.__it == self.size): raise StopIteration
        data = [self.keys[self.__it], self.data[self.__it]]
        self.__it += 1
        return data
    def __len__(self):
        return self.size
    def __bool__(self):
        return bool(self.keys)
    def __repr__(self):
        return repr(dict(zip(self.keys, self.data)))


    def __init__(
        self, 
        keys:(list,Array)=[], 
        data:(list,Array)=[],
        keys_type:E_DATA_TYPE=E_DATA_TYPE.AUTO,
        data_type:E_DATA_TYPE=E_DATA_TYPE.AUTO
        ):
        self.__keys=Array(keys, data_type=keys_type)
        self.__data=Array(data, data_type=data_type)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, new_keys:(list,Array)):
        self.__keys.data = new_keys

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data:(list,Array)):
        self.__data.data = new_data

    @property
    def size(self):
        return len(self.keys)
        
    def append(self, key, data):
        self.keys.append(key)
        self.data.append(data)
    def insert(self, index, key, data):
        self.keys.insert(index, key)
        self.data.insert(index, data)
    def update(self, index, key, data):
        self.keys.update(index, key)
        self.data.update(index, data)
    def delete(self, index):
        del self.keys[index]
        del self.data[index]
    def indexes(self, key):
        return [i for i in range(self.size) if key == self.keys[i]]
    def index(self, key):
        return self.indexes(key)[0] or -1  
