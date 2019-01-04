#Dictionary is a mutable unorder key-value container. The key of dictionary have to be immutable

#define dictionary
population = { 'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print("dictionary is:", population)
print('')

#add key-value element
population = { 'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print("dictionary is:", population)
population['Taipei'] = 5
print("after add one key-value element into dictionary:", population)
print('')

#find whether key exist in dictionary or not
population = { 'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print("dictionary is:", population)
print("Does key 'Taipei' exist in dictionary?", 'Taipei' in population)
print('')

#get dictionary value by key
population = { 'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print("dictionary is:", population)
#better way => python will not get error
print("search dictionary value by key 'Taipei':", population.get('Taipei'))
#not better way => python will get error
#print("search dictionary value by key 'Taipei':", population['Taipei'])
print('')

#nest dictionary
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print("dictionary is:", elements)
elements ['hydrogen']['is_noble_gas'] = False
elements ['helium']['is_noble_gas'] = True
print("Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries:", elements)

#identity operator( is , is not ) vs. comparison operators( != , == )
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print('a:', a)
print('b:', b)
print('c:', c)
print('a == b', a == b)
print('a is b', a is b)
print('a == c', a == c)
print('a is c', a is c)
print('')
