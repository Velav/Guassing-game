import random

name = input("What is your name???")

print("Good luck", name,"!!!")

words = ['gaming', 'greenville', 'snowrunner', 'ets2', 'ats', 'msfs', 'Swfl', 'fs22', 'freeways', 'trailmakers',
         'bloxbrug', 'ptfs', 'cdid', 'flightline', 'erlc', 'bedwars']

word = random.choice(words)

print("Guess the characters of the word!")

guesses = ''

turns = 12

while turns > 0:
    
    failed = 0

    for char in word:
        
        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1
        
    if failed == 0:
        print("You Win, Congratulations!!!")

        print("The word is: ", word)
        break
    guess = input("guess a charchter:")

    guesses = guesses + guess

    if guess not in word:

        turns -=1

        print("Wrong")

        print("You have", + turns, 'more guesses')


        if turns == 0:
            print("You Loose, better luck next time!")
