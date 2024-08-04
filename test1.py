print('test')



for i in range(1,4,1):
    print(i)

for i in range(1,4,2):
    print(i*2)

for i in range(4,0,-1):
    print("$"*i)


mysum = 0
start = 3
end = 5
for i in range(start,end+1):
    mysum += i

print(mysum)

test_string = "We want to remove the nth character from this string"
n = 8

print(test_string[:n-1] + test_string[n:])

my_string = "How many times is the letter e in this string?"

i = 0
for n in my_string:
    if n in 'es':
        i += 1
print(f"number of times 'e' is repeated := {i}")

for i in 'uneet':
    print(i)

s = 'abca'
seen =''
for char in s:
    if char not in seen:
        seen += char
    print(seen)


guess = 0
x = int(input("Enter an integer: "))
while guess**2 <= x:
    guess += 1
if guess**2 == x:
    print(f"square root of {x}" is {guess})
else:
    print(f"{x}, is not a perfect square root.")
