#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they
#guessed too low, too high, or exactly right.
#(Hint: remember to use the user input lessons from the very first exercise)
#Extras:
    #Keep the game going until the user types “exit”
    #Keep track of how many guesses the user has taken,
    #and when the game ends, print this out.
import random

rand = random.randint(1,9)
a = ""
count = 0

while a != "exit":

    a = input("Guess a number between 1-9, or type 'exit' to quit: ")
    count += 1
    
    if a == str(rand):
        print("You guessed right!")
        print("It took you %d tries!" %count)
        count = 0
    elif a < str(rand):
        print("Your number is lower")
    else:
        print("Your number is higher")
