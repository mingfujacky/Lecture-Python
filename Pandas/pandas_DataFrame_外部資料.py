import pandas as pd

a = pd.read_csv('covid19.csv')   #header = 0, index_col = 'country_ch'
b = pd.read_json('covid19.json')
c = pd.read_excel('covid19.xlsx')

url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, keep_default_na = False)
d = tables[0].head(10)

df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index=['王小明','李小美','陳大同','林小玉'],
                   columns=['國文','英文','數學','自然','社會'])
df.to_csv('scores.csv')
