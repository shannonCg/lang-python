# variable defined inside function has the local scope
def some_function():
    word = "say hello"
#outside the function cannot call the variable
#print(world)
print()


# variable defined outside functions has the global scope
other_word = "hello"
def other_function():
    #we can call the variable inside the function
    print(other_word)
other_function()
print()


#we cannot modify global variable value in function
other_word = "hello"
def other_function():
    #we cannot modify global variable value
    #other_word += "hi"
    other_word
other_function()
print(other_word)
print()


#the way to change global variable in function is pass the variable to function as an argument
other_word = "hello"
def other_function():
    return other_word + "~ hi"
other_word = other_function()
print(other_word)
print()


#variable scope priority: local > global
str = "Global variable"
def print_priority():
    #if we comment local variable, the global variable will be printed
    #str = "Local variable"
    print(str)
print_priority()