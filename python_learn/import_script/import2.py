#we want to use other python script and this script is in the same directory,
#we can use 'import script_name'
import test_for_import2

#it will get NameError: name 'num' is not defined
#print(num)

#if we want to get another script method or variable,
#we need to use like [import_name].[method or variable]
print(test_for_import2.num)