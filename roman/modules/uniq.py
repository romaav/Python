def get_unique_list(l):
    return list(set(l))


def get_unique_list2(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list
