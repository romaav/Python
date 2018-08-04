from modules.uniq import get_unique_list, get_unique_list2
from modules.dif import get_dif5_list, get_dif2_list
from modules.sorting import get_sort_reverse_list

l = [4, 4, 5, 5, 2, 1, 0, 10, 10, 4]

print('m with sort ={}'.format(get_unique_list(l)))

print('m without sort ={}'.format(get_unique_list2(l)))
print('list dif 5 ={}'.format(get_dif5_list(l)))
print('list dif 2 ={}'.format(get_dif2_list(l)))
print('list sort and reverse ={}'.format(get_sort_reverse_list(l)))
print('list original ={}'.format(l))
