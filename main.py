from NewEve import check_type


@check_type
def test(p1, p2:(list, tuple, dict), p3:str='', p4=True):
    return p1

if __name__ == '__main__':
    m_str = 'OwnDBrdata=xxx-OwnDBOwnDBrdata=xxy-OwnDB'
    print(m_str.split('OwnDBrdata=')) 
    print(test(0,{'a':89}, p4=False))
    pass