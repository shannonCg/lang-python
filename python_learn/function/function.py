#define function
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius **2

print("the cylinder volume with height {} and radius {} is {}".format(10, 3, cylinder_volume(10, 3)))
print()

#if the function doesn't declear return value, then the function will return default value: none
def say_hello():
    print("Hello!")
value = say_hello()
print("function return value is ", value)
print()

#default function argument
def cylinder_volume(height, radius=3):
    pi = 3.14159
    return height * pi * radius **2

print("the cylinder volume with height {} and default radius 3 is {}".format(10, cylinder_volume(10)))
print("the cylinder volume with height {} and radius {} is {}".format(10, 5, cylinder_volume(10, 5)))
print()

#pass argument by positon or name
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius **2

print("the cylinder volume with height {} and radius {} is {}".format(10, 3, cylinder_volume(10, 3)))
print("the cylinder volume with height {} and radius {} is {}".format(10, 5, cylinder_volume(radius=5, height=10)))
print()