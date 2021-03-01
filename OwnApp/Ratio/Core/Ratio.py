'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from NewEve import load_ui
from OwnDB  import Database, Table, ColumnInfo

class Ratio():
    def __init__(self):
        #UI
        ui_path = './Ratio.ui'
        self.window  = load_ui(ui_path)
        self.widgets = self.__get_widgets__()
        self.__connect__()

        #DATABASE
        self.database = Database('Ratio')


    def __get_widgets__(self):
        pass

    def __connect__(self):
        pass