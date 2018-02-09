# Write a program (function!) that takes a list and returns a new list that contains all
# the elements of the first list minus all the duplicates.

# Extras:

    # Write two different functions to do this - one using a loop and
    # constructing a list, and another using sets.
    # Go back and do Exercise 5 using sets, and write the solution for
    # that in a different function.

x = [1, 1, 2, 2, 3, 4 ,5 ,6 ,6 ,7 ,7 ,7 ,8 ,9 ,10, 10, 11, 12]
def convertListSets(lista):
    lista = set(lista)
    lista = list(lista)
    return lista
#extra
def convertListLoop(lista):
    b = []
    for i in lista:
        if i not in b:
            b.append(i)
    return b        
    
print("Removing duplicates from list [1, 1, 2, 2, 3, 4 ,5 ,6 ,6 ,7 ,7 ,7 ,8 ,9 ,10, 10, 11, 12]")
print(convertListSets(x))
#extra
print(convertListLoop(x))
