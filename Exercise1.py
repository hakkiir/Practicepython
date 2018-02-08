#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will
#turn 100 years old.
#Extras:
    #Add on to the previous program by asking the user for another
    #number and printing out that many copies of the previous message.
    #(Hint: order of operations exists in Python)
    #Print out that many copies of the previous message on separate lines.
    #(Hint: the string "\n is the same as pressing the ENTER button)

name = input("Give me your name: ")
age = int(input("Give me your age: "))
#extra
otherNumber = int(input("Give me another number: "))
turn100 = 2018+100-age

for i in range(0, otherNumber):
     print("%s will turn 100 years old in year %d" % (name, turn100))
