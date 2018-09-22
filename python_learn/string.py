string = 'Hello world I aM coding'

#trim string: string[start: end: step]
print("string => ", string)
print("string[6:11:1] => ", string[6:11:1])
print("string[6:11:2] => ", string[6:11:2])
print("string[6:11:3] => ", string[6:11:3])
print('------------------------')

#loop string backword: string[::-1]
print("string => ", string)
print("string[::-1] => ", string[::-1])
print("string[::-2] => ", string[::-2])
print('------------------------')

#find string length: len(string)
print("string => ", string)
print("len(string) => ", len(string))
print('------------------------')

#test string is digit: string.isdigit(), is alphabetic
print("string => ", string)
print("string.isdigit() => ", string.isdigit())
print("string.isalpha() => ", string.isalpha())

_string = 'Hello'
print("string => ", _string)
print("string.isdigit() => ", _string.isdigit())
print("string.isalpha() => ", _string.isalpha())

num = '50'
print("num => ", num)
print("num.isdigit() => ", num.isdigit())
print("num.isdigit() => ", num.isalpha())
print('------------------------')

#look for word within string: string.find(word)
print("string => ", string)

word = 'hello'
print("word => ", word)
print("string.find(word) => ", string.find(word))

word = 'Hello'
print("word => "+word)
print("string.find(word) => ", string.find(word))
print('------------------------')

#trim string from specific character: string[string.find(word)]
print("string => ", string)

word = 'I'
print("word => ", word)
print("string[string.find(word):] => ", string[string.find(word):])
print('------------------------')

#change first character of every word in string to uppercase: string.title()
print("string => ", string)

print("string.title() => ", string.title())
print('------------------------')

#transfer string into list of characters: list(string)
print("string => ", string)

print("list(string) => ", list(string))
print('------------------------')

#transfer string to uppercase: string.upper(), to lowercase: string.lower()
print("string => ", string)

print("string.upper() => ", string.upper())
print("string.lower() => ", string.lower())
print('------------------------')

#swap case character of string: string.swapcase()
print("string => ", string)

print("string.swapcase() => ", string.swapcase())
print('------------------------')

#join a list of strings into one string separacted by the input string: inputString.join(strings)
strings = ['dan', 'mike', 'rob']
print("strings => ", strings)

print("' '.join(strings) =>", ' '.join(strings))
print("'_'.join(strings) =>", '_'.join(strings))
print('------------------------')

#count how many times a character sequence occurs in a string: string.count(character)
print("string => ", string)

character = 'i'
print("character => ", character)
print("string.count(character) => ", string.count(character))

character = 'o'
print("character => ", character)
print("string.count(character) => ", string.count(character))
print('------------------------')

#replace a part of string with another string: string.replace(origin,new)
print("string => ", string)

new = 'fishing'
print("new => ", new)

origin = 'coding'
print("origin => ", origin)
print("string.replace(origin,new) => ", string.replace(origin,new))

origin = 'oding'
print("origin => ", origin)
print("string.replace(origin,new) => ", string.replace(origin,new))

origin = 'o'
print("origin => ", origin)
print("string.replace(origin,new) => ", string.replace(origin,new))

origin = 'b'
print("origin => ", origin)
print("string.replace(origin,new) => ", string.replace(origin,new))
print('------------------------')

#split the string by separactor: string.split(separactor, separate times)
print("string => ", string)

newString = string.split(" ", 3);
print("separate string => ", newString);

string = 'f++d+'
newString = string.split("+");
print("separate string => ", newString);
