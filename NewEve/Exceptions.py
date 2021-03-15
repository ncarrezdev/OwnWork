'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
class Exceptions():
    @staticmethod
    def TypeException(expected_type, obtained_type):
        if(type(expected_type) == tuple):
            expected_type = expected_type[0]
        return Exception('BAD TYPE - Wrong data type : expected '+str(expected_type)+' got '+str(obtained_type))
    @staticmethod
    def NotImplementedException(function_called):
        return Exception('NOT IMPLEMENTED - Virtual function : '+str(function_called))
    @staticmethod
    def ExistingData(data):
        return Exception('EXISTING DATA - Value already exists : '+str(data))
    @staticmethod
    def SizeException(max_size, asked_size):
        return Exception('BAD SIZE - Can\'t exceed '+str(max_size)+' , got '+str(asked_size))