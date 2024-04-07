def filter_list(l):
    new_l = []
    for i in l:
        if isinstance(i, int):
            new_l.append(i)


#Best Solution Was:
# def filter_list(l):
#   'return a new list with the strings filtered out'
#   return [i for i in l if not isinstance(i, str)]