import collections.abc
'''
    python built-in function: map

    * map(function, iterable,...):
        Return an iterator that applies function to every item of iterable, yielding the results.
'''

def print_result(nums):
    print('nums', nums)
    str_nums = map(num_change_to_str, nums)
    print('str_nums', list(str_nums))
    print("----------------------------")


def num_change_to_str(num):
    return 'num:'+str(num)
numbers = [1, 2, 3, 4, 5]
print_result(numbers)
numbers = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10]
        ]
print_result(numbers)
print()


def num_change_to_str(nums):
    m = map(lambda num: 'num:'+str(num), nums)
    return list(m)
numbers = [1, 2, 3, 4, 5]
# print_result(numbers) #compiled error
numbers = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10]
        ]
print_result(numbers)
print()


def num_change_to_str(nums):
    if isinstance(nums, collections.abc.Iterable):
        m = map(lambda num: 'num:' + str(num), nums)
        return list(m)
    else:
        return 'num:'+str(nums)
numbers = [1, 2, 3, 4, 5]
print_result(numbers)
numbers = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10]
        ]
print_result(numbers)