import pandas as pd
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index=['王小明','李小美','陳大同','林小玉'],
                   columns=['國文','英文','數學','自然','社會'])
#資料排序, df內容不變
a = df.sort_values(by = '數學', ascending = False)
b0 = df.sort_index(axis = 0, ascending = False)  #0軸 by 橫列索引
b1 = df.sort_index(axis = 1, ascending = False)  #1軸 by 直欄標籤
b2 = df.sort_index()                             # default is 0

#資料修改, df就地更改
df.loc['王小明', '數學'] = 10
df.loc['王小明', :] = 20

#資料刪除, df內容不變
c1 = df.drop('王小明', axis = 0) #axis = 0 可省略不寫
c2 = df.drop(['王小明','林小玉'])
c3 = df.drop('數學', axis = 1)
c4 = df.drop(['數學','自然'], axis = 1)
c5 = df.drop(df.index[1:3], axis = 0)   #axis = 0 可省略不寫
c6 = df.drop(df.columns[1:3], axis = 1)

#資料新增
df.loc['陳彼得'] = [30, 35, 40, 45, 50]    #就地更改
new_rows = pd.DataFrame({'國文':{'張阿華':30},
                         '英文':{'張阿華':35},
                         '數學':{'張阿華':40},
                         '自然':{'張阿華':45},
                         '社會':{'張阿華':50},
                         })
d1 = pd.concat([df,new_rows], ignore_index=False) #True代表放棄原來的index, 變成整數的index
df.loc[:,'體育'] = [90, 91, 92, 93, 94]   #就地更改
#df['體育'] = [90, 91, 92, 93, 94]       #就地更改

