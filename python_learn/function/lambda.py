#create anonymous function by lambda expression
#function definition
def multiply(x, y):
    return x * y
print(multiply(3, 4))
#lambda expression
mult = lambda x, y: x * y
print(mult)
print(mult(3, 4))
print()

#use map() function that takes a function and iterable as inputs, and returns an iterator
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

#averages = list(map(mean, numbers))
averages = list(map(lambda list: sum(list) / len(list) , numbers))
print("original list:", numbers)
print("after mapping the list by averaging every list:", averages)
print()

#use filter() function that takes a function and iterable as inputs, and returns an iterator
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

#short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda x: len(x) < 10, cities))
print("original list:", cities)
print("after filter the cities which name is less than 10 characters long", short_cities)