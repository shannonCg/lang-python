#use list comprehension to create list concisely
cities = ['taipei', 'new york', 'tokyo']
print("city:", cities)

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print("capitalized city:", capitalized_cities)
print("-------------------")
#comprehension way
capitalized_cities2 = [ city.title() for city in cities]
print("capitalized city:", capitalized_cities2)
print()

#conditionals in list comprehension
square = [ x**2 for x in range(9) if x % 2 == 0]
print("square:", square)
print()

square2 = [ x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print("num:", square2)
print()
