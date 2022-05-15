def linear_search(mylist, given_element):
    for element in range(len(mylist)):
        if mylist[element]== given_element:
            return element
    
    else:
        return "Element not found"
        
        
print(linear_search([1, 2, 3, 4, 5, 6], 5))