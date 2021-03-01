'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
def flatten_lists(T):
    if (not type(T) == tuple): return (T,)
    elif len(T) == 0: return ()
    else: return flatten_lists(T[0]) + flatten_lists(T[1:]) 