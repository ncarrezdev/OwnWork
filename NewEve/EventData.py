'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from OwnObject import OwnSimpleObject

class EventData(OwnSimpleObject):        
    def __init__(
        self, 
        data             = None, 
        auto_notify:bool = False
        ):
        self.__data = data
        self.__bindings = []
        self.__auto_notify = auto_notify

    @property
    def data(self):
        return self.__data
     
    @data.setter   
    def data(self, new_data):
        self.__data = new_data
        if(self._auto_notify):
            self.notify()
            
    def notify(self):
        for function in self._bindings:
            function()
            
    def bind(
        self, 
        function_to_call:callable
        ):
        self._bindings.append(function_to_call)