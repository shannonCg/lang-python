# zip is the function that can mix mulitple list into a combined tuples list and return an iterator
items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']
weights = [15, 34, 42, 120, 20]
prices = [1.1, 3, 0.5, 10, 1]
print("item:", items)
print("weight:", weights)
print("price:", prices)

print("mix item, weight, and price into one list:", list(zip(items, weights, prices)))
print()

# iterate the zip
items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']
weights = [15, 34, 42, 120, 20]
prices = [1.1, 3, 0.5, 10, 1]
print("item:", items)
print("weight:", weights)
print("price:", prices)

for item, weight, price in zip(items, weights, prices):
    print("item {} has the weight {} and price {}".format(item, weight, price))
print()

#unzip a combined tuples list
manifests = [('bananas', 15, 1.1), ('mattresses', 34, 3), ('dog kennels', 42, 0.5), (
'machine', 120, 10), ('cheeses', 20, 1)]
print("manifest:", manifests)
Items, Weights, Prices = zip(*manifests)
print("take manifest apart:", Items, Weights, Prices)
print()

#enumerate is the function that return a iterator contain index and item of list
letter = ['a', 'b', 'c', 'd', 'e']
print("letter:", letter)
for index, item in zip(range(len(letter)), letter):
    print("index {} of letter is {}".format(index, item))
print("--------------------------")
#above for loop is equal to use enumerate function
for index, item in enumerate(letter):
    print("index {} of letter is {}".format(index, item))
print()
