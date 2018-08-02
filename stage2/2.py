l = [4, 5, 5, 2, 1, 1, 0, 10, 10, 4, 0]
m_first_method = []
def get_function_m_first(l):
    return list(set(l))
print('m ={}'.format(get_function_m_first(l)))

def get_l_dif5_result(l):
    return [i for i in l if i % 5 == 0 and i != 0]
print('get_l_dif5_result ={}'.format(get_l_dif5_result(l)))
