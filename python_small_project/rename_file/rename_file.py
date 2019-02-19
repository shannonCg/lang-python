import os

"""
    rename the file name
"""

def show_dir():
    save_path = os.getcwd()
    print("Current Working Directory is :", save_path)

def rename_file():
    #find all file name from a folder
    dir_path = r"C:\Users\user\python_practice\python_small_project\rename_file\prank"
    file_name = os.listdir(dir_path)

    #change to rename file's folder
    show_dir()
    os.chdir(dir_path)
    show_dir()

    #remove number in every file name
    translation_table = dict.fromkeys(map(ord, '1234567890'), None)
    for name in file_name:
        new_file_name = name.translate(translation_table)
        os.rename(name, new_file_name)


rename_file()

