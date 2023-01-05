import pandas as pd

# 测试表格
des = r'E:\Develop\Project\test_file'
des_books = des + '\\' + 'day5.xlsx'

# 读取一个表格
books = pd.read_excel(des_books, index_col='ID')

# 算出最后的折扣价,两列可以直接相乘
# books['Price'] = books['ListPrice']*books['Discount']

# 循环写法,从其中的某一段技术需要用到这个循环for i in range（5,16）
for i in books.index:
    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

print(books)
