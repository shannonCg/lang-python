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

#docStrings: you can write the description for function
def readable_timedelta(days):
    #use the Google format
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    Returns:
        string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return  "{} week(s) and {} day(s)".format(weeks, remainder)

print(readable_timedelta(10))