#import entire module: import [module_name]
import import_entire_module2

#it will get NameError: name 'num' is not defined
#print(num)

#if we want to get module's function, class or variable,
#we need to use: [module_name].[module's function, class or variable]
print(import_entire_module2.num)
import_entire_module2.print5()