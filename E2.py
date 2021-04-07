num = int(input("Enter a number: "))
check = int(input("Enter a number to check: "))
if num%4 == 0:
    print(str(num) + " is divisible by 4")
elif num%2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")
if num%check == 0:
    print(str(num) + " divides evenly by " + str(check))
else:
    print(str(num) + " does not divide evenly by " + str(check))
