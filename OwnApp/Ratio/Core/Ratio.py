'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from OwnDB  import Database, Table, ColumnInfo
from NewEve import load_ui, get_user_path, get_folder_list

class Ratio():
    def __init__(self):
        import os
        self.__app_name = 'Ratio'
        self.__u_folder = get_user_path()
        #UI
        ui_path = './'+self.__app_name+'.ui'

        #DATABASE
        self.__database = Database(self.__app_name)
        db_folder = [f for f in get_folder_list(self.__u_folder) if f == self.__app_name]
        if(db_folder): 
            #Loading DB
            self.__database.load(os.path.join(self.__u_folder, db_folder[0]))
        else:
            #Building DB manually / default DB
            db = self.__database
            db.append("")

    def __del__(self):
        import os
        self.__database.save(os.path.join(self.__u_folder, self.__app_name))

    def __get_widgets__(self):
        pass

    def __connect__(self):
        pass