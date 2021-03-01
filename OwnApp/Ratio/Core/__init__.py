'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
import os, sys
this_file_path = os.path.abspath(os.path.dirname(__file__))
if(this_file_path not in sys.path):
    sys.path.append(this_file_path)

#---------------------------------------------------------

from Ratio import *