def show(str_to_show):
    size = int(len(str_to_show)/2)
    key = str_to_show[size:]
    str_to_show = str_to_show[:size]

    int_key = []
    int_str = []
    res = []
    for i in range(len(str_to_show)):
        int_key.append(ord(key[i]))
        int_str.append(ord(str_to_show[i]))
        if(int_str[i] - int_key[i] < 0):
            int_str[i] = int_str[i] + 256
        int_str[i] = int_str[i] - int_key[i]
        res.append(chr(int_str[i]))
    return ''.join(res)
    