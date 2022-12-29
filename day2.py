import pandas as pd

xlsx = r'D:\Desktop\1505385\test.xlsx'
xlsx2 = r'D:\Desktop\1505385\test2.xlsx'
# 读取表格到内存
people = pd.read_excel(xlsx)

# 打印多少行，多少列
print(people.shape)

# 打印列名
print(people.columns)

#打印全部数据
#print(people)

#打印头部数据，默认五行
print(people.head())

#打印头部数据，指定3行
print(people.head(3))

#打印尾部数据
print(people.tail(3))

# 从第二行读取数据
people2 = pd.read_excel(xlsx2, header=1)
print('从第二行读\n{}'.format(people2.columns))

# 自定义标题
people2 = pd.read_excel(xlsx2, header=None, index_col='ID')
people2.columns = ['ID','Type','Title','First','middle','last']
people2.set_index('ID',inplace=True)
people2.to_excel(xlsx2)