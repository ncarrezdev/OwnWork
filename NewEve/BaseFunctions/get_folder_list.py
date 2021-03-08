'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
def get_folder_list(path):
    import os
    return [f for f in os.listdir(path) if os.isfile(os.path.join(path, f))]