import math

class NameOfClass:

    gvar = 'This is global'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)


my_class = NameOfClass(1, 2)
print(type(my_class))
print(my_class)
print(my_class.param2)
my_class.some_method()
print(my_class.gvar)

class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circum(self):
        return self.radius * self.pi * 2



my_circle = Circle()
print(my_circle.get_circum())
print(my_circle.area)

class Animal():

    def __init__(self):
        print("Animal Created")
    def who_am_i(selfself):
        print("I am an animal")
    def eat(selfs):
        print("I am eating")



myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()







#distance =
#y2-y1 / x2-x1


class Cylinder:

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius


    def volume(self):
        return Cylinder.pi * self.radius**2 *self.height

    def surface_area(self):
        return 2 * self.radius * Circle.pi * (self.height + self.radius)
        pass

c=Cylinder(2,3)
print(c.volume())
print(c.surface_area())



class Line:
    def __init__(self, coor1, coor2):
        self.x1, self.y1 = (coor1)
        self.x2, self.y2 = (coor2)

    def distance(self):
        line_qr= ((self.x2 - self.x1)**2 + (self.y2 -self.y1)**2)
        return math.sqrt(line_qr)
    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.slope())
print(li.distance())

class Account:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f" Account Owner: {self.owner} \n Account balance: ${self.balance}"

    def deposit(self,dep_amount):
        self.balance += dep_amount
        print("deposit accepted")
        #return self.balance no need tio return

    def withdraw(self,wid_amount):
        if wid_amount <= self.balance:
            self.balance -= wid_amount
            print("withdraw accepted")
        else:
            print('Funds Unavailable!!')
        #return self.balance no need to return

account1=Account('Jose', 100)
print(account1)
account1.deposit(100)
print(account1.balance)
account1.withdraw(300)
account1.deposit(400)
print(account1.balance)
print(account1)