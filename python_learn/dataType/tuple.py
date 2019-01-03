#Tuple is similar to list; that is, they are both in order.
#However unlike list, tuple is immutable. We can't add, delete element from tuple or sort them

#define tuple
location = (13.111, 103.111)
print("latitude: ", location[0])
print("longitude: ", location[1])
print("")

#define tuple can omit parentheses
location = 13.111, 103.111
print("latitude: ", location[0])
print("longitude: ", location[1])
print("")

#tuple unpacking:
#we can unpack tuple to assign element into multiple variables without having to
#access them one by one
dimensions = 52, 40, 100
length, width, hight = dimensions
print("The dimensions are {}x{}x{}".format(length, width, hight))