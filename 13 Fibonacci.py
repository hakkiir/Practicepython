#Write a program that asks the user how many Fibonnaci numbers to
#generate and then generates them. Take this opportunity to think
#about how you can use functions. Make sure to ask the user to enter
#the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next
#number in the sequence is the sum of the previous two numbers in the sequence.
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibonacci():
    count = int(input("How long sequence of fibonacci numbers to generate?: "))
    i = 1
    if count == 0:
        fibo = []
    elif count == 1:
        fibo = [1]
    elif count == 2:
        fibo = [1,1]
    elif count > 2:
        fibo = [1,1]
        for i in range (1, count-1):
            fibo.append(fibo[i] + fibo[i-1])
            i += 1
    return fibo
                
print(fibonacci())

