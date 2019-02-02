#rename imported module name: import [module_name] as [new_module_name]
import  rename_imported_module as test

list = [1, 2, 3, 4, 5]
print("origin list:", list)
print("after adding 5 for each element of list:", test.add_five(list))
print("print __name__ variable of test_for_rename_imported_module file:", __name__)

