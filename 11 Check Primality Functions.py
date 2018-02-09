#Ask the user for a number and determine whether the number is prime or not.
#(For those who have forgotten, a prime number is a number that has no divisors.).
#You can (and should!) use your answer to Exercise 4 to help you.
#Take this opportunity to practice using functions.

def check_prime(num):
    
    if num == 1:
        prime = False
    elif num == 2:
        prime = True
    else:
        prime = True
        for i in range(2, (num//2)+1):
            if num%i == 0:
                prime = False
                break
    return prime

def printAnswer(number):
    prime = check_prime(number)
    if prime:
        print("%d is a prime." %number)
    else:
        print("%d is not a prime" %number)
    
num = int(input("Put a number and see if it is a prime or not: "))

printAnswer(num)
