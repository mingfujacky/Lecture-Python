import pandas as pd
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index=['王小明','李小美','陳大同','林小玉'],
                   columns=['國文','英文','數學','自然','社會'])

#以直欄標籤取值
a1 = df['國文']                 #series
a2 = df[['國文']]               #dataframe
a3 = df[['國文','英文','數學']]  #dataframe
#a4 = df['王小明']               #error

#以橫列索引和直欄標籤取值

b1 = df.loc['林小玉', '社會']                    #int
b2 = df.loc['林小玉', ['社會', '國文']]           #series
b3 = df.loc['王小明',:]                         #series
b4 = df.loc[:,'國文']                           #series
b5 = df.loc[:,['國文']]                         #dataframe
b6 = df.loc[['林小玉','王小明'], ['社會', '國文']] #dataframe
b7 = df.loc['王小明':'陳大同', '國文':'數學']      #dataframe
b8 = df.loc['王小明']                           #series
#b8 = df.loc['數學']                             #error

#指定欄位以條件式判斷取值
#boolean indexing: Using boolean array (series) to index select rows
c1 = df[[False, True, True, False]]  #不取row1&4, 取row2&3, dataframe
c2 = df['國文'] >= 80                 #series
c3 = df[df['國文'] >= 80]            # dataframe

#以values取值
d1 = df.values              #Numpy ndarray

#以橫列編號和直欄編號取值
e1 = df.iloc[3,4]           #int
e2 = df.iloc[0,[0,4]]       #series
e3 = df.iloc[[0,1],[2,3]]   #dataframe
e4 = df.iloc[0:3,2:5]       #dataframe
e5 = df.iloc[2,:]           #series
e6 = df.iloc[:2, 2:5]       #dataframe
e7 = df.iloc[1:, 2:5]       #dataframe

#取得最前及最後幾筆資料
f1 = df.head(3)             #dataframe
f2 = df.tail()              #dataframe
