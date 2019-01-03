#List and string are almost similarly,
# that is, index, len, slice and membership operators used on list also suitable for string
#but the big different from list and string is list is mutable and string is immutable.

#list is mutable
list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things2 = list_of_random_things
print("list: " + str(list_of_random_things))
list_of_random_things[0] = 2
print("change first element of list: " + str(list_of_random_things))
list_of_random_things[1:3] = [4.5, 'change']
print("change second and third element of list: "+ str(list_of_random_things))
print(list_of_random_things2)
print('')

#variable hold immutable object
num1 = 1
num2 = num1
num1 = 2
print(num1)
print(num2)

name1 = 'John'
name2 = name1
name1 = 'Sam'
print(name1)
print(name2)
print('')

#list index
list_of_random_things = [1, 3.4, 'a string', True]
print("list: " + str(list_of_random_things))
print("fist of list: " + str(list_of_random_things[0]))
print("last of list: " + str(list_of_random_things[-1]))
print('')

#slice and list length
list_of_random_things = [1, 3.4, 'a string', True]
print("list: " + str(list_of_random_things))
print("slice second to third element: " + str(list_of_random_things[1:3]))
print("slice first to third element: " + str(list_of_random_things[:3]))
print("slice third to end element: " + str(list_of_random_things[2:]))
print("length of list: "+ str(len(list_of_random_things)))
print('')

#membership operators: in / not in
list_of_random_things = [1, 3.4, 'a string', True]
print("list: " + str(list_of_random_things))
print("1 exist in list: "+ str(1 in list_of_random_things))
print("2 not exist in list: "+ str(2 not in list_of_random_things))
print('')

#length of list
list_of_random_things = [1, 3.4, 'a string', True]
print("list: " + str(list_of_random_things))
print("length of list: "+ str(len(list_of_random_things)))
print('')

#max/min of list(only can compare with same datatype)
list_of_random_things = [1, 3.4, -1, 5]
print("list: " + str(list_of_random_things))
print("max of list: "+ str(max(list_of_random_things)))
print("min of list: "+ str(min(list_of_random_things)))
print('')

#sort list(return copy of list)
list_of_random_things = [1, 3.4, -1, 5]
print("list: " + str(list_of_random_things))
print("sort list in order from small to large : "+ str(sorted(list_of_random_things)))
print("reverse list in order from large to small: "+ str(sorted(list_of_random_things, reverse=True)))
print('')

#join every list element with specific word convert to string(join() is string method,
# and it only joins string list)
list_of_random_things = ['John', 'Jim', 'Sam']
print("list: " + str(list_of_random_things))
print("join list with character '-': "+ "-".join(list_of_random_things))
print('')

#append elemnt to the end of list
list_of_random_things = [1, 3.4, 'a string', True]
print("list: " + str(list_of_random_things))
list_of_random_things.append('zzz')
print("after append element 'zzz' to list: "+ str(list_of_random_things))
print('')

a = [1, 2, 3]
b = [4, 5, 6]
print("list a: " + str(a))
print("list b: " + str(b))
result_1 = a.append(b)
result_2 = a + b
print("result_1 = a.append(b): "+str(result_1))
print("result_2 = a+b: "+str(result_2))

