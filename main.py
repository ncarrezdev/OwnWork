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
    str_to_compress = "nfogbnubqO GQFN<FBGQOFGBQIBDV QEBFIqdfq isbdqpfgbqdjkfnq df n^ùwfobnsf gsqfgsqwfwkjonfgpw m<vbwfbghjq<wbfioghednfuq bhqdkfjlngkd<f fwfxklxklnboxgf nxl"
    binned_str = binary_compression(str_to_compress)
    print(binned_str[0])
    v = int(binned_str[0],2)
    binned_v = "{0:b}".format(v)
    res_str = binary_decompression(binned_v, binned_str[1])
    print(res_str)
    print(res_str == str_to_compress)
    

