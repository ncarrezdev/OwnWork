from OwnCrypt.show     import show
from OwnCrypt.scramble import scramble

def complete_uncrypt(string_to_uncrypt):
    res = string_to_uncrypt
    res = show(res)
    res = scramble(res, True)
    res = show(res)
    res = scramble(res, True)
    return res