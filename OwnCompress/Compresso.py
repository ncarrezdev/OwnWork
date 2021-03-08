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
    cpy_map = map_to_sort
    quantity=[]
    for i in range(len(cpy_map)):
        if(cpy_map[i][1] not in quantity):
            quantity.append(cpy_map[i][1])

    for i in range(len(quantity)-1):
        if(quantity[i]<quantity[i+1]):
            buff = quantity[i]
            quantity[i] = quantity[i+1]
            quantity[i+1] = buff
            i=0

    sorted_vals=[]
    for q in quantity:
        for i in range(len(cpy_map)):
            if(q == cpy_map[i][1]):
                sorted_vals.append(cpy_map[i][0])
    return sorted_vals

@check_time
def get_compression_map(string_to_compress):
    sorted_map = sort_by_quantity(map_char_quantity(string_to_compress))
    nb_bits = len(bin(len(sorted_map))[2:])
    std_bit_str = '0'*nb_bits
    compression_map = []
    for i in range(len(sorted_map)):
        binary_form = (std_bit_str + bin(i)[2:])[-nb_bits:]
        compression_map.append([sorted_map[i], binary_form])
    return compression_map