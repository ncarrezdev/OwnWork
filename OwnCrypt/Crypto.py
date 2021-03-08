'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
class Crypto():
    def __init__(self, complexity:int = 1):
        self.__complexity = complexity

    def crypt(self, str_to_crypt:str, reverse:bool=False):
        res = str_to_crypt
        for i in range(self.__complexity):
            if(reverse):
                res = self.__scramble__(res)
                res = self.__hide__(res)
            elif(not(reverse)):
                res = self.__hide__(res, True)
                res = self.__scramble__(res, True)
        return res

    def __hide__(str_to_hide, reserve:bool=False):
        if(reserve):
            from random import randrange
            key = []
            int_str = []
            for i in range(len(str_to_hide)):
                int_str.append(ord(str_to_hide[i]))
                rand = randrange(0,256)
                excluded = list(range(0,32)) + [127] + list(range(244,255))
                while(
                    (rand + int_str[i])%256 in excluded  or
                    rand in excluded
                    ):
                    rand = randrange(0,256)
                key.append(rand)
                int_str[i] = (key[i] + int_str[i])%256
            int_str += key
            res = []
            for i in range(len(int_str)):
                res.append(chr(int_str[i]))
            return ''.join(res)
        else:
            size = int(len(str_to_hide)/2)
            key = str_to_hide[size:]
            str_to_hide = str_to_hide[:size]

            int_key = []
            int_str = []
            res = []
            for i in range(len(str_to_hide)):
                int_key.append(ord(key[i]))
                int_str.append(ord(str_to_hide[i]))
                if(int_str[i] - int_key[i] < 0):
                    int_str[i] = int_str[i] + 256
                int_str[i] = int_str[i] - int_key[i]
                res.append(chr(int_str[i]))
            return ''.join(res)

    def __scramble__(str_to_scramble, reverse:bool=False):
        def __swap__(item_to_swap, central_index, delta):
            index_minus = central_index - delta
            index_plus  = central_index + delta
            if(index_plus >= len(item_to_swap)):
                index_plus = index_plus - len(item_to_swap)
            temp = item_to_swap[index_minus]
            item_to_swap[index_minus] = item_to_swap[index_plus]
            item_to_swap[index_plus] = temp
            pass

        res = list(str_to_scramble)
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