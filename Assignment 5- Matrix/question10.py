def flat_list(mylist):
    new_list = []
    empty_list = []
    for element in mylist:
        for j in element:
            new_list.append(j)
    
    for i in new_list:
        if i in empty_list:
            continue
        else:
            empty_list.append(i)
    
    return empty_list
    
print(flat_list([[1],[2,3,4],[2]]))