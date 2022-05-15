def checkSum(list, k):
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                if list[i] + list[j] == k:
                    return True
                else:
                    continue
            else:
                continue
    
    return False
    
print(checkSum([1,4,2,3,5], 99))
