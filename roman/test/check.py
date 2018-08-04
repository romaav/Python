from modules.uniq import get_unique_list, get_unique_list2
from modules.dif import get_dif5_list, get_dif2_list
from modules.sorting import get_sort_reverse_list

l = [7, 2, 2, 4, 4, 5, 5, 10, 10]

# check unique_list
unique_list = get_unique_list(l)
assert unique_list == [2, 4, 5, 7, 10]

# check unique_list2
unique_list2 = get_unique_list2(l)
assert unique_list2 == [7, 2, 4, 5, 10]

# check dif5_list
dif5_list = get_dif5_list(l)
assert dif5_list == [5, 5, 10, 10]

# check dif2_list
dif2_list = get_dif2_list(l)
assert dif2_list == [2, 2, 4, 4, 10, 10]

# check sort_reverse_list
sort_reverse_list = get_sort_reverse_list(l)
assert sort_reverse_list == [10, 10, 7, 5, 5, 4, 4, 2, 2]

print('все ЗАЕБИСЯ!')