def power_set(mylist):
    if len(mylist) == 0:
        return [[]]
    subset = power_set(mylist[1:])
    return subset + [[mylist[0]] + element for element in subset]
    
    
def i_am_a_genius(mylist):
    final_list = []
    new_list = []
    for element in power_set(mylist):
        if ("a" in element) and ("b" in element) and ("c" in element):
            final_list.append(element)
        else:
            continue
    for i in final_list: 
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list
print(i_am_a_genius(['a', 'a', 'a', 'c', 'b']))