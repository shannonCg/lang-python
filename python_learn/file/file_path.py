#operate file path
import os.path

def show_file_info(file_name):
    print("*file name:", file_name)

    absolute_path = os.path.abspath(file_name)
    print("absolute path of file:", absolute_path)

    base_name = os.path.basename(absolute_path)
    print("base name of absolute path:", base_name)

    directory_path = os.path.dirname(absolute_path)
    print("directory path of absolute path:", directory_path)

    split_names = os.path.split(absolute_path)
    print("split file name from absolute path:", split_names)

    split_drive_names = os.path.splitdrive(absolute_path)
    print("split drive name from absolute path:", split_drive_names)


file_names = ['camelot.txt', '.']
for name in file_names:
  show_file_info(name)
  print()
print("---------------------------")


camelot_name = 'camelot.txt'
abs_path_of_camelot = os.path.abspath(camelot_name)
dir_path_of_camelot = os.path.dirname(abs_path_of_camelot)
my_file_name = 'my_file.txt'
join_path_of_my_file = os.path.join(dir_path_of_camelot, my_file_name)
abs_path_of_my_file = os.path.abspath(my_file_name)
print("join path of my_file.txt:", join_path_of_my_file)
print("absolute path of my_file.txt:", abs_path_of_my_file)
print("---------------------------")

# find the pathnames matching a specific pattern
import glob

def search_file(search_pattern):
    files = glob.glob(search_pattern)
    print("*find file with pattern:", search_pattern)
    for file in files:
        print("file name:", file)
        print("absolute path of file:", os.path.abspath(file))
    print()

search_pattern = r"p*"
search_file(search_pattern)
search_pattern = r"C:/Users/user/**/**/p*"
search_file(search_pattern)
search_pattern = r"../../p*"
search_file(search_pattern)
print("---------------------------")

#find all files and driectories in specific directory recursivly
import os
package_import = os.walk("../package_import")
for dirname, subdirs, files in package_import:
    print("*dirname:", dirname)
    print("subdirs:", subdirs)
    for file in files:
        print("file:", file)
        print("absolute path of file:", os.path.join(os.path.abspath(dirname), file))
    print()



