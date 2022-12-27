import pandas as pd

# 数据字典
map1 = {
    'ID':[1,2,3,4],
    'Name':['张三','李四','王五','刘六']
}
# 定义一个数据填充表格
df = pd.DataFrame(map1)
# 设置索引列
df = df.set_index('ID')
# 输出表格位置
dest = r'D:\Develop\StudyFile\test.xlsx'
# 输出生成表格
df.to_excel(dest)
print(df)
print('已输出到{}'.format(dest))

note = '1.安装pandas \r 2.使用pandas写入数据创建表格'
print(note)