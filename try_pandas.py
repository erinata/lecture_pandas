import numpy as np
import pandas as pd

n = 100

t = pd.date_range('20190130', periods=n)

# print(t)

df = pd.DataFrame(np.random.randn(n, 10), index=t, columns=list('ABCDEFGHIJ'))

# print(df.head())

# print(df.head(10))

# print(df.tail(4))

print(df.describe())

print(df.T)

print(df.sort_values(by='C'))
#print(df.head().sort_values(by='C'))


print(df['D'])

print(df[0:3])


print(df[df.B>0].head())











