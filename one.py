print("hello")

def func():
    print("func() in 1.py")

print("TOP LEVEL in 1.py")

if __name__ == "__main__":
    print("'1.py is being run directly!")
else:
    print("1.py had been imported")