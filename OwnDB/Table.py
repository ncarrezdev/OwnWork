from NewEve import Array
from NewEve import OwnSimpleObject
from NewEve import Exceptions
from NewEve import E_UNIQUE_TYPE
from NewEve import E_DATA_TYPE
from NewEve import check_type


class ColumnInfo(OwnSimpleObject):
    def __init__(
        self, 
        name='', 
        data_type=None,
        data_default=None, 
        unique_type:E_UNIQUE_TYPE=E_UNIQUE_TYPE.NONE
        ):
        self.__name    = name
        self.__type    = data_type or type(data_default)
        self.__default = data_default
        self.__unique  = unique_type
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def type(self):
        return self.__type
    
    @property
    def default(self):
        return self.__default
    
    @default.setter
    def default(self, new_default):
        self.__default = new_default
    
    @property
    def unique(self):
        return self.__unique


class TableException(Exceptions):pass

class Table(Array):
    append = property()    
    insert = property()    
    update = property()    
    delete = property()    
    indexes= property()    
    index  = property()

    def __init__(self, name:str=''):
        Array.__init__(self, data_type=E_DATA_TYPE.NONE)
        self.__name = name
    
    @property
    def name(self):
        return self.__name  

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @check_type
    def append_row(self, data:(list, tuple)):self.__append_row__(data)
    @check_type
    def insert_row(self, index:int, data:(list, tuple)):self.__insert_row__(index, data)
    @check_type
    def update_row(self, index:int, data:(list, tuple)):self.__update_row__(index, data)
    @check_type
    def get_row(self, index:int): return self.__get_row__(index)
    @check_type
    def delete_row(self, index:int):self.__delete_row__(index)

    def indexes_row(self, data): return self.__indexes_row__(data)
    def index_row(self, data): return self.indexes_row(data)[0] or -1

    @check_type
    def append_col(self, column:ColumnInfo):self.__append_col__(column)
    @check_type
    def insert_col(self, index:int, column:ColumnInfo):self.__insert_col__(index, column)
    @check_type
    def update_col(self, index:int, column:ColumnInfo):self.__update_col__(index, column)
    @check_type
    def get_col(self, index:int): return self.__get_col__(index)
    @check_type
    def delete_col(self, index:int):self.__delete_col__(index)

    def indexes_col(self, name): return self.__indexes_col__(name)
    def index_col(self, name): return self.indexes_col(name)[0] or -1

    @check_type
    def update_col_data(self, index:int, data:(list, tuple)):self.__update_col_data__(index, data)
    @check_type
    def get_col_data(self, index:int): return self.__get_col_data__(index)

    def indexes_col_data(self, data): return self.__indexes_col_data__(data)
    def index_col_data(self, data): return self.indexes_col_data(data)[0] or -1


    def __append_row__(self, data):
        if(len(data) > self[0].size):
            TableException.SizeException(self[0].size-1, len(data))
        Array.append(self, Array(data, E_DATA_TYPE.NONE))
    def __insert_row__(self, index, data):
        if(index >= self.size-1):
            TableException.SizeException(self.size-2, index)
        if(len(data) > self[0].size):
            TableException.SizeException(self[0].size-1, len(data))
        Array.insert(self, index+1, Array(data, E_DATA_TYPE.NONE))
    def __update_row__(self, index, data):
        if(index >= self.size-1):
            TableException.SizeException(self.size-2, index)
        if(len(data) > self[0].size):
            TableException.SizeException(self[0].size-1, len(data))
        Array.update(self, index+1, Array(data, E_DATA_TYPE.NONE))
    def __delete_row__(self, index):
        if(index >= self.size-1):
            TableException.SizeException(self.size-2, index)
        Array.delete(self, index+1)
    def __get_row__(self, index):
        if(index >= self.size-1):
            TableException.SizeException(self.size-2, index)
        return self[index+1]

    def __indexes_row__(self, data):
        return [i-1 for i in range(self.size) if data in self[i]]


    def __append_col__(self, column):
        if(not self):
            Array.append(self, Array(data_type=E_DATA_TYPE.NONE))
        self[0].append(column)
        for row in self[1:]:
            row.append(column.default)        
    def __insert_col__(self, index, column):
        if(index >= self[0].size):
            TableException.SizeException(self[0].size-1, index)
        self[0].insert(index, column)
        for row in self[1:]:
            row.insert(index, column.default)
    def __update_col__(self, index, column):
        if(index >= self[0].size):
            TableException.SizeException(self[0].size-1, index)
        self[0].update(index, column)
    def __delete_col__(self, index):
        if(index >= self[0].size):
            TableException.SizeException(self[0].size-1, index)
        self[0].delete(index)
        for row in self[1:]:
            row.delete(index)
    def __get_col__(self, index):
        if(index >= self[0].size):
            TableException.SizeException(self[0].size-1, index)
        return self[0][index]

    def __indexes_col__(self, name):
        return [i for i in range(self[0].size) if name == self[0][i].name]


    def __update_col_data__(self, index, data):
        if(index >= self[0].size):
            TableException.SizeException(self[0].size-1, index)
        if(len(data) > self.size-1):
            TableException.SizeException(self.size-1, len(data))
        self[1:].update(index, data)
    def __get_col_data__(self, index):
        if(index >= self[0].size):
            TableException.SizeException(self[0].size-1, index)
        return self[1:][index]

    def __indexes_col_data__(self, data):
        return [i for i in range(self[0].size) if data in [self[1:][i]]]
        