names = ['dan', 'rob', 'mike','jen', 'john', 'shannon', 'jonny', 'jason']

#method 1: access element
for i in names:
    print (i)
print('')

#method 2: access index and element
for i in range(0, len(names)):
    print(str(i+1)+':'+names[i])
print('')

#method 3: skip element
for i in range(0, len(names), 3):
    print(names[i])
print('')

#method 4: range(int) => make increasing number list
for i in range(10):
    print(i)
print('')