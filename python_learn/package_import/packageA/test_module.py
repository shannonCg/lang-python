#when we import module where is in the package, there are two way to import them
#1. absolute import ([A] for short)
#2. relative import ([R] for short)


#import same package's module => packageA_module
#[A] way
#from python_learn.package_import.packageA import packageA_module
# packageA_module.printLocation()
#[R] way (not work in python3)
#from . import packageA_module
#packageA_module.printLocation()


#import same package's module specific function => printLocation() in packageA_module
#[A] way
# from python_learn.package_import.packageA.packageA_module import printLocation
# printLocation()
#[R] way (not work in python3)
# from .packageA_module import printLocation
# printLocation()


#import another package's module specific function => printLocation() in packageB_module
#[A] way
# from python_learn.package_import.packageB.packageB_module import printLocation
# printLocation()
#[R] way (not work in python3)
# from ..packageB.packageB_module import printLocation
# printLocation()

#import parent module => top_module
#[A] way
# from python_learn.package_import import top_module
# top_module.printLocation()
#[R] way (not work in python3)
# from .. import top_module
# top_module.printLocation()

#import sub package module of moduleA => sub_packageA_module
#[A] way
# from python_learn.package_import.packageA.sub_package_of_packageA.sub_packageA_module import printLocation
# printLocation()
#[R] way (not work in python3)
# from .sub_package_of_packageA.sub_packageA_module import printLocation
# printLocation()