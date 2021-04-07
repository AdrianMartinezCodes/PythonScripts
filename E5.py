import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
#soln 1

for i in a:
    if i in b and not i in c:
        c.append(i)
print(c)

#soln 2

a = random.sample(range(1,20),5)
b = random.sample(range(1,20),10)
c = []
for i in a:
    if i in b and not i in c:
        c.append(i)
print(c)
