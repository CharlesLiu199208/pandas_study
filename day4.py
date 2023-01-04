from datetime import date

import pandas as pd

# 测试表格
des = r'E:\Develop\Project\test_file'
des_books = des + '\\' + 'Books_t.xlsx'


# 月份累增到年的函数
def add_month(d, md):
    '''
    :param d: 日期，年月日
    :param md:换算月份的给定值
    :return:递增日期
    '''
    # 年份,md 整除12的值
    yd = md // 12

    # 新的月份等于，当期月份 + md 总数取12的余数
    m = d.month + md % 12

    # 超过12个月换算成需要累增的年份
    if m != 12:
        yd += m // 12

    # 返回一个时间，年份加换算要增加的年份
    return date(d.year + yd, m, d.day)


# 读取表格
books2 = pd.read_excel(des_books)
# print(books2)#不能直接跳过空行，打印出来空行也会读到

# 跳过行读取skiprows，跳过列读取usecols = ’C,D,E‘ 或usecols = 'C:D'
books = pd.read_excel(des_books, skiprows=6, usecols='C:F', index_col=None, dtype=str)
# print(books)

# ID 列，一个序列
# print(books['ID'])

# 为book 的 ID 列第1个单元格赋值
books['ID'].at[0] = 100
# print(books['ID'])

'''循环把ID 赋值
默认是float类型，需要在读取的时候转换下内容类型dtype = {'ID':str},全部转换dtype = str

'''
# 定义一个起始时间
start = date(2018, 1, 1)
for i in books.index:
    # 循环序号加1
    books['ID'].at[i] = i + 1

    # 交替循环,如果i对2取余等于0等于Yes，否则等于No
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'

    '''
    start + timedelta(days=i);起始日期天数加i
    timedelta 只能加天，时，分，秒，毫秒，周
    '''
    # books['Date'].at[i] = start + timedelta(days=i)

    # 年份循环增加
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)

    # 月份累增到年自动换算,
    books['Date'].at[i] = add_month(start,i)

# print(books)

# 输出到一个表
#设置索引
books.set_index('ID', inplace=True)
books.to_excel(des + '/' + 'output.xlsx')

# 直接改单元格值的方法
for i in books.index:
    # books 的i行，i从0开始，索引，ID列
    books.at[i,'ID'] = i + 1
    books.at[i,'InStore'] = 'Yes' if i % 2 == 0 else 'No'
    books.at[i,'Date'] = add_month(start,i)
books.set_index('ID', inplace=True)
books.to_excel(des + '/' + 'output2.xlsx')