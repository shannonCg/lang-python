#calling the read method with an integer
with open("camelot.txt") as f:
    print(f.read(2))
    print(f.read(8))
    print(f.read())
print("-------------")

#read line by line
with open("camelot.txt") as f:
    print(f.readline())
    #because each line still has its newline character attached, we can remove this using string function:strip()
    print(f.readline().strip())
    print("The end")
print("--------------")

#another method to read file content line by line
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        # camelot_lines.append(line)
        camelot_lines.append(line.strip())
print(camelot_lines)