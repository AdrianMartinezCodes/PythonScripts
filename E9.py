import random

compare = random.randint(1,9)
stop,count = 0,0

while stop != "exit":
    user = int(input("Please input a number: "))
    count += 1
    if user == compare:
        print("You guessed correctly")
    elif user > compare:
        print("You guessed too high")
    else:
        print("You guess too low")
    stop = str(input("To quit type \'exit\'. Or press enter to play again."))
               
print("You guessed" + str(count) + "times.")
