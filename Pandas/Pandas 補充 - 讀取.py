import numpy as np
import pandas as pd
# syntax: assign row index and column lable
df = pd.DataFrame(np.arange(12).reshape((4, 3)))
df.index = ['R1', 'R2', 'R3', 'R4']
df.columns = ['A', 'B', 'C']

# syntax2: assign row index and column lable
df2 = pd.DataFrame(np.arange(12).reshape((4, 3)),
                   index = ['R1', 'R2', 'R3', 'R4'],
                   columns = ['A', 'B', 'C'])
# 使用方括弧取值
foo1 = df['A']  # read 1 column Series
foo2 = df[['A', 'C']] # read 2 columns DataFrame
foo3 = df[:2] # read 2 rows DataFrame

# 使用索引器取值 loc
spam1 = df.loc[:,:]  # DataFram
spam2 = df.loc[:, 'A']  # Series
spam3 = df.loc[:, ['A', 'C']] # DataFrame
spam4 = df.loc['R1',:]  # Series
spam5 = df.loc[['R1','R2'],:] # DataFrame
spam6 = df.loc['R1',['A', 'C']] # Series
spam7 = df.loc[['R1'],['A', 'C']] # DataFrame
spam8 = df.loc['R1':'R3','A':'C'] # DataFrame


# 使用索引器取值 iloc
egg1 = df.iloc[1, 1]   # int
egg2 = df.iloc[1:, 1]  # Series
egg3 = df.iloc[1:, :2]  # DataFrame
