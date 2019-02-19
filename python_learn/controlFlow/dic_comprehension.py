#use dic comprehension to create dictionary concisely
fruits = ['apple', 'banana', 'mango']
word_length = {word:len(word) for word in fruits}
print(word_length)
print()

#combine with enumerate
word_index = { index:word for index, word in enumerate(fruits)}
print(word_index)
print()

#combine with dictionary function: items
word_double_length = { key:value*2 for key, value in word_length.items()}
print(word_double_length)
print()