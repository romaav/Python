l = [4, 5, 5, 2, 1, 1, 0, 10, 10, 4, 0]
m_first_method = []

print('original list l = {}'.format(l))
for i in l:  # first method for m
    if i not in m_first_method:
        m_first_method.append(i)
print('первый способ m = {}'.format(m_first_method))

m_second_method = list(set(l))  # second method for m
print('второй способ m = {}'.format(m_second_method))

l_even_number = l[::2]
print('элементы списка на четных позициях l = {}'.format(l_even_number))

l_dif5_result = [i for i in l if i % 5 == 0 and i != 0]  # dif 5
print('элементы списка кратные 5 l = {}'.format(l_dif5_result))


l_dif2_result = [i for i in l if i % 2 == 0 and i != 0]  # dif 2
print('четные элементы списка l = {}'.format(l_dif2_result))

l_for_sort = l[::]
l_for_sort.sort(reverse=True)  # sort with reverse
print('отсортировонный список в порядке убывания l = {}'.format(l_for_sort))
print('original list l = {}'.format(l))