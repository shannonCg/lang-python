import pandas as pd
import numpy as np

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print()

#apply(): applying function to the data
# if True:
if False:
    print(df.apply(np.mean))
    print(df.apply(lambda x : x.max() - x.min()))
    print(df.apply(lambda x : x+10))
    print()

#map(): create a new Series by applying operated function and only be used on Series
#applymap(): create a new DataFrame by applying operated function and only be used on DataFrame
if True:
# if False:
    print(df['one'].map(lambda x : x+10))
    print()
    print(df.applymap(lambda x: x+10))

