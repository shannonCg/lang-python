#we can alias import's script name
import python_learn.import_script.test_for_import3 as test

list = [1, 2, 3, 4, 5]
print("origin list:", list)
print("after adding 5 for each element of list:", test.add_five(list))
print("__name__ variable of import3.py:", __name__)
