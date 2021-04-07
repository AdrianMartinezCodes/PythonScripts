def sent_rev(a_sent):
    return " ".join(a_sent.split()[::-1])

user_in = str(input("Please enter a sentence: "))
print(user_in)
print(sent_rev(user_in))
