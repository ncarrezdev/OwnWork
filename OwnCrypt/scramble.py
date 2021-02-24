def __swap__(item_to_swap, central_index, delta):
    index_minus = central_index - delta
    index_plus  = central_index + delta
    if(index_plus >= len(item_to_swap)):
        index_plus = index_plus - len(item_to_swap)
    temp = item_to_swap[index_minus]
    item_to_swap[index_minus] = item_to_swap[index_plus]
    item_to_swap[index_plus] = temp
    pass

def scramble(item_to_scramble, reverse:bool=False):
    res = list(item_to_scramble)
    n_range = range(         0, len(res), 1)
    r_range = range(len(res)-1, 0-1     ,-1)

    range_to_use = n_range
    if(reverse):
        range_to_use = r_range
    for i in range_to_use:
        if(
            (i%10 == 2) or
            (i%10 == 4) or
            (i%10 == 8)
            ):
            __swap__(res, i, 3)
        elif(
            (i%10 == 0) or
            (i%10 == 6)
            ):
            __swap__(res, i, 4)
        elif(
            (i%10 == 1) or
            (i%10 == 3) or
            (i%10 == 9)
            ):
            __swap__(res, i, 2)
        elif(
            (i%10 == 5) or
            (i%10 == 7)
            ):
            __swap__(res, i, 1)
    return ''.join(res)
    