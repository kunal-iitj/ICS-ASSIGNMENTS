def power_set(mylist):
    if len(mylist) == 1:
        return [[], [mylist[0]]]
    sub_set = power_set(mylist[1:]) # here we are defining a subset
    return sub_set + [element.append(mylist[0]) for element in sub_set]
print(power_set([1, 2, 3, 4, 5]))