class OwnSimpleObject(object):
    def __repr__(self):
        members = dir(self)
        public_members = [member for member in members if(not('__' in member))]
        members_values = [self.__getattribute__(member) for member in public_members]
        return str([value for value in members_values if value != None])