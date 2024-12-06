import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

index_x = ['王小明','李小美','陳大同','林小玉']
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index=['王小明','李小美','陳大同','林小玉'],
                   columns=['國文','英文','數學','自然','社會'])

#g1 = df.plot(kind = 'bar', title = '長條圖', figsize = [10, 5])
#g2 = df.plot(kind = 'barh', title = '橫條圖', figsize = [10, 5])
#g3 = df.plot(kind = 'bar', stacked = True, title = '堆疊圖', figsize = [10, 5])
g4 = df.plot(kind = 'pie', legend = False, subplots = True, title = '圓餅圖', fontsize = 8, figsize = [10, 10])
#plt.legend(loc="best", fontsize=8)
plt.show()