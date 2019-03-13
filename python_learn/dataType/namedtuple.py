from collections import namedtuple

'''
    Named tuples assign meaning to each position in a tuple.
    They add the ability to access fields by name instead of position index.
'''

#simple
#define 1
# Point = namedtuple('Point', 'x, y')
#define 2
Point = namedtuple('Point', ['x', 'y'])

#instantiate with positional or keyword arguments
p = Point(3, y=4)
print(p)
print(p[0] + p[1])
print(p.x + p.y)
print("-------------")

#unpack like a regular tuple
a, b = p
print(a + b)
print("-------------")

#make a new instance from an existing squence or iterable
#   classmethod somenamedtuple._make(iterable)
t = [10, 11]
p2 = Point._make(t)
print(p2)
print("-------------")

#usually used with 'csv' or 'sqlite3' module
students = [(1, '王小明'), (2, '王大明'), (3, '美美'), (4, '胖胖')]
Student = namedtuple('Student', ['stdno', 'name'])
named_students = map(Student._make, students)
named_students = list(named_students)
print(named_students)
for student in named_students:
    print("no:{} is {}".format(student.stdno, student.name))
