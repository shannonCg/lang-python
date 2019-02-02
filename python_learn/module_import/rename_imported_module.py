def add_five(num_list):
    return [n + 5 for n in num_list]
print("print __name__ variable of rename_imported_module file:", __name__)
#we can use __name__ variable to let code runned when the script in directly run by python,
#and let code not runned when the script in import to other script
if "__main__" == __name__:
    print("run by main")