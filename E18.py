import random


def gen_num():
    return str(random.randint(1000,9999))

def checker(usr_input,num):
    bull,cow = 0,0
    for i in range(len(usr_input)):
            if usr_input[i] == num[i]:
                cow +=1
            elif usr_input[i] in num:
                bull += 1
    return cow,bull

def game():
    num = gen_num()
    count = 0
    stop = False
    while stop != True:
        count += 1
        user = str(input("Guess a number: "))
        cow,bull = checker(user, num)
        if cow != 4:
            print(cow, "Cows, ", bull, " bull")
        else:
            stop = True
    print("the number was " + num)    
    print("You guessed it right", cow, "cow", "in only ", count, " turns")
    

    

if __name__=="__main__":
    game()
        
                          
