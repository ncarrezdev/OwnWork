'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
class OwnSimpleObject(object):
    def __repr__(self):
        members = dir(self)
        public_members = [member for member in members if(not('__' in member))]
        members_values = [self.__getattribute__(member) for member in public_members]
        return str([value for value in members_values if value != None])