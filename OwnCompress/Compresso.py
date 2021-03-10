'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from NewEve import check_time

def map_char_quantity(string_to_map):
    res = []
    c_list = []
    for c in string_to_map:
        if(c in c_list):
            index = c_list.index(c)
            res[index][1] += 1
        else:
            c_list.append(c)
            res.append([c,1])
    return res

def sort_by_quantity(map_to_sort):
    quantity=[]
    for i in range(len(map_to_sort)):
        if(map_to_sort[i][1] not in quantity):
            quantity.append(map_to_sort[i][1])

    for i in range(len(quantity)-1):
        if(quantity[i]<quantity[i+1]):
            buff = quantity[i]
            quantity[i] = quantity[i+1]
            quantity[i+1] = buff
            i=0

    sorted_vals=[]
    for q in quantity:
        for i in range(len(map_to_sort)):
            if(q == map_to_sort[i][1]):
                sorted_vals.append(map_to_sort[i][0])
    return sorted_vals

@check_time
def binary_compression(string_to_compress):
    char_quantity_map = map_char_quantity(string_to_compress)
    sorted_char_map = sort_by_quantity(char_quantity_map)

    nb_bits = len(bin(len(sorted_char_map))[2:])
    bit_str = '0'*nb_bits
    compression_dict={}
    for i in range(len(sorted_char_map)):
        binary_i = (bit_str + bin(i)[2:])[-nb_bits:]
        compression_dict[sorted_char_map[i][0]] = binary_i

    res = ''
    for c in string_to_compress:
        res += compression_dict[c]
    return res, [c for c in compression_dict]

@check_time
def binary_decompression(string_to_decompress, char_list):
    nb_bits = len(bin(len(char_list))[2:])
    bit_str = '0'*nb_bits
    compression_dict={}
    for i in range(len(char_list)):
        binary_i = (bit_str + bin(i)[2:])[-nb_bits:]
        compression_dict[binary_i] = char_list[i]
    
    res = ''
    for i in range(len(string_to_decompress)):
        start = (-nb_bits*(i+1)) 
        if((i+1)*nb_bits > len(string_to_decompress)):start = 0
        stop  = (-nb_bits*i or None)
        v_to_convert = string_to_decompress[start:stop]
        if(len(v_to_convert) != nb_bits):
            zeros_to_add = '0'*(nb_bits-len(v_to_convert))
            v_to_convert = zeros_to_add + v_to_convert
        res = compression_dict[v_to_convert] + res
        if((i+1)*nb_bits > len(string_to_decompress)):break
    return res

def smart_compression(string_to_compress):
    pass