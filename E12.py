import random

def sorter(a_list):
    return [i for i in a_list if i not in a_list[1:len(a_list)-1]]

a = [5, 10, 15, 20, 25]
print(sorter(a))
b = random.sample(range(1,50),20)
print(sorter(b))


#prefered soln
#def list_ends(a_list):
#    return [a_list[0], a_list[len(a_list)-1]]
