import math

def prime_checker(a):
    diviser_list =[]
    #check = int(math.sqrt(a))
    for i in range(1,a):
        if a%i == 0:
            diviser_list.append(i)
    return(diviser_list)


num = int(input("Give me a number to check: "))
check = prime_checker(num)
if len(check) != 1:
    print(str(num) + " is not prime")
else:
    print(str(num) + " is prime")
