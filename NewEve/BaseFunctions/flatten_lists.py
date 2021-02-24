def flatten_lists(T):
    if (not type(T) == tuple): return (T,)
    elif len(T) == 0: return ()
    else: return flatten_lists(T[0]) + flatten_lists(T[1:]) 