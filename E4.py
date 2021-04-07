num = int(input("Please enter a number to divide: "))
diviser_list = []
for i in range(1,num):
    if num%i == 0:
        diviser_list.append(i)
print(diviser_list)
