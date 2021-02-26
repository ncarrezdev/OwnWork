from NewEve import E_UNIQUE_TYPE
from OwnDB import Database
if __name__ == '__main__':
    print(str.__name__)
    print(eval('str'))
    m_db = Database()
    m_db.load('./m_db')
    print(m_db)
    m_db.save('./m_db2')