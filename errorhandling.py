
def add(n1,n2):
    return(n1+n2)

try:
    result = 10 + '10'
except:
    print("you dont know how to add")


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('cant raise to power for str')


x=5
y=0
try:
    z=x/y
except ZeroDivisionError:
    print("Cant divide by zero")
finally:
    print("All Done")

def ask():
    while True:
        try:
            num=float(input("please input number:"))
        except:
            print("An error occured! Please try again!")
            continue
        else:
            print("Input an integer: ", num)
            print("Thank you, your number squared is: ", num**2)
            break
ask()


