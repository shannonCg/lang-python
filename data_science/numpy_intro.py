import numpy as np

'''
Numpy is a library that provides functions that are especially useful when you have to 
work with large arrays and matrices of numeric data, like doing matrix matrix multiplications.
'''
if True:
    numbers = [2, 2, 3, 2, 2]
    print("array is ", numbers)
    print("mean of array is ", np.mean(numbers))
    print("median of array is ", np.median(numbers))
    print("standard deviation of array is ", np.std(numbers))


'''
The array object class is the foundation of Numpy, and Numpy arrays are like
lists in Python, except that every thing inside an array must be of the
same type, like int or float.
'''
if False:
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")

    two_D_array = np.array([[1, 2, 3],[4, 5, 6]], float)
    print(two_D_array)
    print("")

'''
You can index, slice, and manipulate a Numpy array much like you would with a
a Python list.
'''
if False:
    array = np.array([1, 4, 5, 8], float)
    print(array)
    print("")
    print(array[1])
    print("")
    print(array[:2])
    print("")
    array[1] = 10.0
    print(array)
    print("")

    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print(two_D_array)
    print("")
    print(two_D_array[1][1])
    print("")
    print(two_D_array[1, :])
    print("")
    print(two_D_array[:, 2])
    print("")

'''
Here are some arithmetic operations that you can do with Numpy arrays
'''
if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    print("array1: ", array_1)
    print("array2: ", array_2)
    print("")
    print(array_1+array_2)
    print("")
    print(array_1-array_2)
    print("")
    print(array_1*array_2)
    print("")

    two_D_array_1 = np.array([[1, 2], [3, 4]], float)
    two_D_array_2 = np.array([[5, 6], [7, 8]], float)
    print("two-D array1: ", two_D_array_1)
    print("two-D array2: ", two_D_array_2)
    print("")
    print(two_D_array_1 + two_D_array_2)
    print("")
    print(two_D_array_1 - two_D_array_2)
    print("")
    print(two_D_array_1 * two_D_array_2)
    print("")

'''
dot product
'''
if False:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    print("array1: ", array_1)
    print("array2: ", array_2)
    print("")
    print(np.mean(array_1))
    print(np.mean(array_2))
    print("")
    print(np.dot(array_1, array_2))

if True:
    a = np.array([1, 2])
    b = np.array([[2, 4, 6], [3, 5, 7]])
    print(np.dot(a, b))
    print()
    c = np.array([[2, 4, 6], [3, 5, 7]])
    d = np.array([[8], [9], [10]])
    print(np.dot(c, d))
