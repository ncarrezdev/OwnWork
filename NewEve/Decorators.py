'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from NewEve import Exceptions

def check_type(f):
    def decorator(*args, **kwargs):
        varnames = f.__code__.co_varnames
        vartypes = f.__annotations__
        for i in range(len(varnames)):
            varname = varnames[i]
            if(varname in vartypes):
                l_type = 0
                if(type(vartypes[varname]) != tuple):
                    l_type = (vartypes[varname],)
                else:
                    l_type = vartypes[varname]
                o_type = 0
                if(i < len(args)):
                    arg_to_check = args[i]
                    o_type = type(arg_to_check)
                elif(varname in kwargs):
                    arg_to_check = kwargs[varname]
                    o_type = type(arg_to_check)
                if(not(o_type in l_type) and o_type != 0):
                    raise Exceptions.TypeException(l_type, o_type)
        return f(*args, **kwargs)
    return decorator

def check_time(f):
    def decorator(*args, **kwargs):
        import time
        start_time = time.time()
        res = f(*args, **kwargs)
        print(f.__name__, '{0:.5f}'.format(time.time() - start_time))
        return res
    return decorator