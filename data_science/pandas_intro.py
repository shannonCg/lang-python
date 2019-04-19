import pandas

'''
Series: the object behavior like list
'''
# if True:
if False:
    series = pandas.Series([4, 7, -5, 3])
    print(series)
    print(series[2])
    print()

#manually assign indices in Series
# if True:
if False:
    series = pandas.Series(['4', '7', '-5', 'aa'], index=['a', 'b', 'c', 'd'])
    print(series)
    print(series['d'])
    print()

#transform dictionary to Series
# if True:
if False:
    dict_data = {'name':'apple', 'birthday':'1996-1-1', 'luckynumber':7}
    series = pandas.Series(dict_data)
    print(series)
    print(series['name'])
    print(series[['name', 'birthday']])
    print()

#use boolean operators to select specific itmes from Series
# if True:
if False:
    cuteness = pandas.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig', 'Puppy', 'Kitten'])
    print(cuteness > 3)
    print()
    print(cuteness[cuteness > 3])
    print("--------------------")

'''
DataFrame: the 2-D array
'''
data = {'name': ['Bob', 'Nancy', 'Amy', 'Elsa', 'Jack'],
        'year': [1996, 1997, 1998, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day': [11, 23, 8, 3, 11]}
# if True:
if False:
    myframe = pandas.DataFrame(data)
    print(myframe)
    print()
    print(myframe['name'])
    print()

#change column order
# if True:
if False:
    myframe2 = pandas.DataFrame(data, columns=['year', 'month', 'day', 'name'])
    print(myframe2)
    print()

#add new column
# if True:
if False:
    myframe3 = pandas.DataFrame(data, columns=['name', 'year', 'month', 'day', 'luckynumber'])
    print(myframe3)
    luckynumber = ['3', '2', '1', '7', '8']
    luckynumber = pandas.Series(luckynumber)
    myframe3['luckynumber'] = luckynumber
    print(myframe3)
    print()

#some column value not be specified
'''
A couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame
'''
# d = {'name': pandas.Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index=['a', 'b', 'c', 'd']),
#      'age': pandas.Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
#      'fare': pandas.Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
#      'survived?': pandas.Series([False, True, True, False])}
d = {'name': pandas.Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index=['a', 'b', 'c', 'd']),
     'age': pandas.Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
     'fare': pandas.Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
     'survived': pandas.Series([False, True, True, False], index=['a', 'b', 'c', 'd'])}
dataFrame = pandas.DataFrame(d)
# if True:
if False:
    print(dataFrame)

#get specific column
# if True:
if False:
    print(dataFrame['name'])
    print(dataFrame.name) #shorthand for dataFrame['name']
    print(dataFrame[['name', 'age']])

#get specific row
# if True:
if False:
    print(dataFrame.loc['a'])
    print(dataFrame.loc[['a', 'c']])

#combine multiple selection requirements through boolean operators like & (and) or | (or)
if True:
#if False:
    print(dataFrame[1:3])
    print(dataFrame[dataFrame.age > 26])
    print(dataFrame[(dataFrame.age > 26) & (dataFrame.survived == True)])
    print(dataFrame[dataFrame.age > 26]['name'])
    print()

#useful function in DataFrame
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pandas.DataFrame(data)

#dtypes: to get the datatype for each column
# if True:
if False:
    print(football.dtypes)
    print()

#describe: useful for seeing basic statistics of the dataframe's numerical columns
# if True:
if False:
    print(football.describe())
    print()

#head: displays the first five rows of the dataset
# if True:
if False:
    print(football.head())
    print()

#tail: displays the last five rows of the dataset
# if True:
if False:
    print(football.tail())
    print()

#info: show data information
# if True:
if False:
    print(football.info())
    print()

#shape: show data (rows, columns)
# if True:
if False:
    print(football.shape)
    print()