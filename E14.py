def sort(a_list):
    return set(a_list)

def sort_list(a_list):
    b = []
    for i in a_list:
        if i in a_list and i not in b:
        #just needed if i not in b:    
            b.append(i)
    return b
    #updated soln below, old soln above, not working
    #return [b.append(i) for i in a_list if i not in b]

def ex_5_sort(first_list,second_list):
    return set(first_list) & set(second_list)

a = ['hi','hi','ok','lol']
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(sort(a))
print(sort_list(a))
print(ex_5_sort(b,c))
