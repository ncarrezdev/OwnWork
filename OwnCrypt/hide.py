from random import randrange
def hide(str_to_hide):
    key = []
    int_str = []
    for i in range(len(str_to_hide)):
        int_str.append(ord(str_to_hide[i]))
        rand = randrange(0,256)
        while(
            (rand + int_str[i])%256 <= 32  or
            (rand + int_str[i])%256 == 127 or
            (rand + int_str[i])%256 >= 244
            ):
            rand = randrange(0,256)
        key.append(rand)
        int_str[i] = (key[i] + int_str[i])%256
    int_str += key
    res = []
    for i in range(len(int_str)):
        res.append(chr(int_str[i]))
    return ''.join(res)
    