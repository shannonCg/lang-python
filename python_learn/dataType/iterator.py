# 'Iterables' are objects that can return one of their element at a time, ex: list
# 'Iterator' is an object that represents a stream of data
# 'Generators' are a way to create iterator using function
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

print(my_range(5))
print(list(my_range(5)))
for i in my_range(5):
    print(i)
print()

# Generator expression
a_list = [x ** 2 for x in range(5)]
print(a_list)
a_iterator = (x ** 2 for x in range(5))
print(a_iterator)
print()

# Add Iterator behavior to your own class
class Reverse:
    """ Iterator for looping over a sequence backwards"""

    """ class initial function """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    """ Return a object with a __next__() function 
        If your class define __next__() function, you can return self
    """
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for i in rev:
    print(i)
print()