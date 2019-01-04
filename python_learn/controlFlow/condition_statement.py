#condition statement: if, elif, else
season = "winter"

if season == "spring":
    print("plant the garden")
elif season == "summer":
    print("water the garden")
elif season == "fall":
    print("harvest the garden")
elif season == "winter":
    print("stay indoors")
else:
    print("unrecognized season")

print("")

#numerical condition: range condition
weight, height = 55, 160
if 18.5 <= weight / (height/100)**2 < 25:
    print("BMI is considered 'normal'")

print("")

#conditions combine with logical operator: and, or, not
is_customer = False
location = "CAN"
if (not is_customer) and (location == "USA" or location == "CAN"):
    print("send email")

print("")

#python non-boolean expression
#following expression is considered to be false by python
# 1. None and False
# 2. zero of any numeric type
# 3. empty sequence and collections
test = None
#test = 'a'
if test:
    print("variable is not None or False, zero, empty sequence or empty collections")
test = 0.0
#test = 1.0
if test:
    print("variable is not zero")
test = ''
#test = {1}
if test:
    print("variable is not empty sequence or empty collections")

