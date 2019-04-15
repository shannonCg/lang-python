def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i < pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

array = [1,9,4,3,2]
print("array is ", array)
sorted_array = quick_sort(array)
print("sort array is", sorted_array)