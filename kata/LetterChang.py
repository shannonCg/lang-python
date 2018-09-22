#Have the function [LetterChanges(str)] take the [str] parameter being passed and modify it using the following algorithm.
#Replace every letter in the string with the letter following it in the alphabet(ie. c becomes d, z becomdes a).
#The capitalize every vowel in this string(a,e,i,o,u) and finally return this modified string.

def LetterChanges(str):
    # chars = list(str.lower())
    vowels = ['a', 'e', 'i', 'o', 'u']
    newChars = []

    for char in str:
        if char.isalpha():
            ordChar = ord(char)
            if 122 == ordChar:
                ordChar = 97
            else:
                ordChar += 1

            char = chr(ordChar)
            if char in vowels:
                char = char.upper()

        newChars.append(char)

    return "".join(newChars)


# keep this functionp call here
raw_input = "abcdz!"
print (LetterChanges(raw_input))

