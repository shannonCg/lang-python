#write file
#1. use built-in function 'open(file_path, file_mode)' can open specific file
#2. file_mode has r:read-only(default value), w:write(it will rewrite file content), a:append to exist file content
#3. if we open the file not exist and file_mode is 'w' or 'a', python will create a new one
#4. every time we open the file, we must finally close the file use built-in function 'close()'
file = open("./my_file.txt", 'w')
file.write("Hello World!")
file.close()

#append txt to file
file = open("./my_file.txt", 'a')
file.write("\nHello World Again!")
file.close()

#read exist file
file = open("./my_file.txt", 'r')
file_data = file.read()
print(file_data)
file.close()
print()

#python provide a special syntax that auto-closes a file for you once you finished using it
with open("./my_file.txt", 'r') as file:
    file_data = file.read()
    print(file_data)