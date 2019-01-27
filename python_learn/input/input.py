# the build-in function that can get the raw input from user: input()
name = input("Enter your name: ")
print("Hello there, {}!".format(name))

# input will take in whatever user type and store it as a string
# hence, you don't want to use string type, you need to convert it.
num = int(input("Enter an integer"))
print("hello"*num)

# the build-in function can interpret string as a Python expression: eval()
result = eval(input("Enter an expression: "))
print(result)