from NewEve import Array
from NewEve import Exceptions
from NewEve import E_DATA_TYPE
from NewEve import check_type
from OwnDB  import Table


class DatabaseException(Exceptions):pass

class Database(Array):
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
    def append(self, table:(Table,str)):
        self.__append__(table)
    @check_type
    def insert(self, index, table:(Table,str)):
        self.__insert__(index, table)
    @check_type
    def update(self, index, table:(Table,str)):
        self.__update__(index, table)
    def delete(self, index):
        self.__delete__(index)
    def get(self, index):
        return self.__get__(index)
    def indexes(self, name):
        return self.__indexes__(name)
    def index(self, name):
        return self.indexes(name)[0] or -1  
        
    def __append__(self, table):
        if(type(table)==str):
            table = Table(table)
        Array.append(self, table)
    def __insert__(self, index, table):
        if(index >= self.size-1):
            DatabaseException.SizeException(self.size-1, index)
        if(type(table)==str):
            table = Table(table)
        Array.insert(self, index, table)
    def __update__(self, index, table):
        if(index >= self.size-1):
            DatabaseException.SizeException(self.size-1, index)
        if(type(table)==str):
            old_table = self[index]
            old_table.name = table
            table = old_table
        Array.update(self, index, table)
    def __delete__(self, index):
        if(index >= self.size-1):
            DatabaseException.SizeException(self.size-1, index)
        Array.delete(self, index)
    def __get__(self, index):
        if(index >= self.size-1):
            DatabaseException.SizeException(self.size-1, index)
        return self[index]
    def __indexes__(self, name):
        return [i for i in range(self.size) if name == self[i].name]
