word = input("Please enter a word: ")
rev_word = word[::-1]
print(rev_word,word)
if word == rev_word:
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindome.")
