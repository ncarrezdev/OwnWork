import os, sys
this_file_path = os.path.abspath(os.path.dirname(__file__))
if(this_file_path not in sys.path):
    sys.path.append(this_file_path)

#---------------------------------------------------------

from Database import *
from Table    import *