#Ask the user for a string and print out whether this
#string is apalindrome or not.
#A palindrome is a string that reads the same forwards and backwards.)

string = input("Give me a word: ")


if string == string[::-1]:
    print(string)
else:
    print("Not a palindrome")
