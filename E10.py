import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[same_num for same_num in a if same_num in b]
d = []
for i in c:
    if i not in d:
        d.append(i)
        
print(d)

a = random.sample(range(1,50),20)
b = random.sample(range(1,50),20)
c=[same_num for same_num in a if same_num in b]
d =[]
for i in c:
    if i not in d:
        d.append(i)
print(c)
