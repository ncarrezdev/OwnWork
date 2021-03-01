'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''
from NewEve import E_UNIQUE_TYPE
from OwnDB import Database
if __name__ == '__main__':
    print(str.__name__)
    print(eval('str'))
    m_db = Database()
    m_db.load('./m_db')
    print(m_db)
    m_db.save('./m_db2')