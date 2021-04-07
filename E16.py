import random
import string
import time

def pass_gen(strength):
    if strength == 'weak':
        return random.choice(['sucks','lol','yes'])
    elif strength == 'strong':
        password = []
        low_letters = set(string.ascii_lowercase)
        upper_letters = set(string.ascii_uppercase)
        numbers = set(str(random.sample(range(0,9),9)))
        symbols = set(string.punctuation)
        for i in range(10):
            password.append(random.choice(list(low_letters|upper_letters|
                                          numbers| symbols)))
        return ''.join(password)

stop = str(input("Type \'stop\' to exit or any key to continue: "))
while stop != 'stop':
    strength = str(input(
        "How strong(Weak,Strong) do you want your password to be? "))
    print(pass_gen(strength))
    stop = str(input("Enter \'stop\' to exit, otherwise new password: "))
