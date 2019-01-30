#handle exception
# try block: the exception can be caught when run this block statement
# except block: when exception is caught, the related statement need to be executed
# finally block: before Python leaves try statement, it will run code in 'finally' block under any condition
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except:
        print("That's not a valid number!")
    finally:
        print("\nAttempted Input\n")
print()

#handle specific exception
#method 1
try:
    x = int(input("Enter a number: "))
except (ValueError, EOFError):
    print("That's not a valid number!")
print()
#method 2
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
except EOFError:
    print("stop the program")
print()

#access error message
#Exception is the base class for all built-in exceptions
try:
    x = int(input("Enter a number: "))
except Exception as e:
    print("Exception occurred: ", e)