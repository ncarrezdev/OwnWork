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