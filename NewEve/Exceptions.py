class Exceptions():
    @staticmethod
    def TypeException(expected_type, obtained_type):
        if(len(expected_type) and type(expected_type) == tuple):
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