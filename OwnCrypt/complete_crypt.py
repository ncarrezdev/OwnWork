from OwnCrypt.hide     import hide
from OwnCrypt.scramble import scramble

def complete_crypt(string_to_crypt):
    res = string_to_crypt
    res = scramble(res)
    res = hide(res)
    res = scramble(res)
    res = hide(res)
    return res