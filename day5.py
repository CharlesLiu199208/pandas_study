import pandas as pd

# 测试表格
des = r'./TestFile'
des_books = des + '\\' + 'day5.xlsx'

def add_2(x):
    return x + 2

# 读取一个表格
books = pd.read_excel(des_books, index_col='ID')

# 算出最后的折扣价,两列可以直接相乘
# books['Price'] = books['ListPrice']*books['Discount']

# 循环写法,从其中的某一段技术需要用到这个循环for i in range（5,16）
# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# 自加,列中所有单元格加2
# books['ListPrice'] = books['ListPrice'] + 2

# 可以使用.apply 里运行函数对单元格进行修改,apply中只填函数名称
# books['ListPrice'] = books['ListPrice'].apply(add_2)

# 也可以写成lambda表达式
books['ListPrice'] = books['ListPrice'].apply(lambda x: x+2)

print(books)
