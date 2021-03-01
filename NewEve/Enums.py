'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from enum import Enum

class E_DATA_TYPE(Enum):
    NONE    = None
    AUTO    = 'AUTO'
    CUSTOM  = 'CUSTOM'
    INTEGER = int
    FLOAT   = float
    STRING  = str
    BOOL    = bool

class E_THREAD_STATE(Enum):
    START = 'START'
    LOOP  = 'LOOP'
    STOP  = 'STOP'
    IDLE  = 'IDLE'
    QUIT  = 'QUIT'

class E_UNIQUE_TYPE(Enum):
    NONE = 'None'
    ALPHABETICAL = 'Alphabet'
    NUMERICAL    = 'Numeric'
    CUSTOM       = 'Custom'