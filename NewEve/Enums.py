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