a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
check = int(input("Enter a numb to check: "))
for i in a:
    if i < check:
        b.append(i)
print(b)
         
