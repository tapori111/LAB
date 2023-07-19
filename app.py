from _ast import Assert
from math import *
from sys import getsizeof

####Number ######
print(3+4.5)

print(pow(3,2))
print(ceil(3.1))



############String#############
print("Hello World")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

phrase = 'Giraffe Academy'

print(phrase.find("D"))

print(3+4.5)

#### input####
def ask():
    while True:
        try:
            num = float(input("Enter a number:"))
        except:
            print("please enter a number")
            continue
        else:
            print('thanks for input:',num)
            return num


#num1=ask()
#num2=ask()

#result = num1 + num2
#print(result)


squares_list = [ pow(num,2) for num in range(12)]
print(squares_list)
squares_dict = {num: pow(num,2) for num in range(12)}
print(squares_dict)
squares_dict = {num: num**2 for num in range(12)}
print(squares_dict)
squares_set = {num**2 for num in range(12)}
print(squares_set)
squares_gen = (num**2 for num in range(12))
print(squares_gen)

L = ["a", "b", "c", "d"]
for el in L:
    print(el)

A = ["a", "b", "c", "d"]
B = ["e", "f", "g", "h"]
for va,vb in zip(A,B):
    print(va,vb)

for i, (va,vb) in enumerate(zip(A,B)):

    print(i,va,vb)


L=[n for n in range(42_000)]
print(sum(L))
print(getsizeof(L))

G=(n for n in range(42000))
print(G)
print(sum(G))
print(getsizeof(G))