'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from NewEve import Map
from OwnCompress import *
if __name__ == '__main__':
    """
    str_to_compress = "nfogbnubqO GQFN<FBGQOFGBQIBDV QEBFIqdfq isbdqpfgbqdjkfnq df n^ùwfobnsf gsqfgsqwfwkjonfgpw m<vbwfbghjq<wbfioghednfuq bhqdkfjlngkd<f fwfxklxklnboxgf nxl"
    binned_str = binary_compression(str_to_compress)
    print(binned_str[0])
    v = int(binned_str[0],2)
    binned_v = "{0:b}".format(v)
    res_str = binary_decompression(binned_v, binned_str[1])
    print(res_str)
    print('res = str_to_compress ?',res_str == str_to_compress)
    """
    m_map = Map()
    m_map.append(0, 'a')
    m_map.append(1, 'b')
    print(m_map)    
    m_map.append('c', 2)