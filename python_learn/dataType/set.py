#Set is an unorder but mutable container. It can collect elements without repeat

#define set
numbers = [1, 2, 3, 5, 3, 2]
unique_numbers = set(numbers)
print("set is:", unique_numbers)
print("")

#add element to set
numbers = [1, 2, 3, 5, 3, 2]
unique_numbers = set(numbers)
print("set is:", unique_numbers)
unique_numbers.add(4)
print("add element '4' to set:", unique_numbers)
print("")

#remove random element from set
numbers = [1, 2, 3, 5, 3, 2]
unique_numbers = set(numbers)
print("set is:", unique_numbers)
unique_numbers.pop()
print("remove random element from set:", unique_numbers)
print("")

#find element exist in set or not
numbers = [1, 2, 3, 5, 3, 2]
unique_numbers = set(numbers)
print("set is:", unique_numbers)
print("is '5' element exists in set:", 5 in unique_numbers)
print("")