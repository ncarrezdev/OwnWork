'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from OwnCompress import *
if __name__ == '__main__':
    ## Comptage bit a bit
    print(int('00000000',2))
    print(int('00000001',2))
    print(int('00000010',2))

    #print(map_char_quantity("Hello World!"))
    #print(sort_by_quantity(map_char_quantity("Hello World!")))
    print(get_compression_map("Hello World!"))