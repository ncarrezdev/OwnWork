'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from NewEve import Array
from NewEve import Exceptions
from NewEve import E_DATA_TYPE
from NewEve import E_UNIQUE_TYPE
from NewEve import check_type
from Table  import Table, ColumnInfo

class DatabaseException(Exceptions):pass

class Database(Array):
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
        
    
    def save(self, folder_path):
        import os
        try:
            os.mkdir(folder_path)
        except:pass
        for table in self:
            file_name = table.name
            file_to_write = open(os.path.join(folder_path, file_name+'.db'), 'w')
            str_to_write = ''
            for column in table[0]:
                str_to_write += 'OwnDBcname='+str(column.name)+'-OwnDB'
                str_to_write += 'OwnDBctype='+str(column.type.__name__)+'-OwnDB'
                str_to_write += 'OwnDBcdefault='+str(column.default)+'-OwnDB'
                str_to_write += 'OwnDBcunique='+str(column.unique)+'-OwnDB'
                str_to_write += '\n'
            str_to_write += '#---\n'
            for row in table[1:]:
                for data in row:
                    str_to_write += 'OwnDBrdata='+str(data)+'-OwnDB'
                str_to_write += '\n'
            file_to_write.write(str_to_write[:-1])
        
    def load(self, folder_path):
        import os
        folder_name = os.path.basename(os.path.normpath(folder_path))
        self.name = folder_name
        self.data = []
        table_files = [file for file in os.listdir(folder_path) if file.endswith('.db')]

        for table_file in table_files:
            new_table = Table(table_file.replace('.db',''))
            opened_file = open(os.path.join(folder_path, table_file), 'r')
            buffer = opened_file.readlines()
            opened_file.close()
            split_index = buffer.index('#---\n')
            for line in buffer[:split_index]:
                name    = line.split('OwnDBcname=')[1].split('-OwnDB')[0]
                dtype   = eval(line.split('OwnDBctype=')[1].split('-OwnDB')[0])
                default = dtype(line.split('OwnDBcdefault=')[1].split('-OwnDB')[0])
                unique  = E_UNIQUE_TYPE[line.split('OwnDBcunique=')[1].split('-OwnDB')[0].split('.')[1]]
                column = ColumnInfo(name, dtype, default, unique)
                new_table.append_col(column)

            for line in buffer[split_index+1:]:
                row   = []
                datas = []
                for val in line.split('OwnDBrdata=')[1:]:
                    val = val.split('-OwnDB')[0]
                    datas.append(val)

                for i in range(new_table[0].size):
                    row.append(new_table[0][i].type(datas[i]))
                new_table.append_row(row)
            self.append(new_table)