import pandas as pd

#字典
d = {'x':100, 'y':200, 'z':300}
l1 = [100,200,300]
l2 = ['x','y','z']

# 创建序列，同字典很相似,#字典转序列
s1 = pd.Series(d)
# print(s1.index)

# 两个列表创建序列
s2 = pd.Series(l1,index=l2)
# print(s2)

# 直接写入创建
s3 = pd.Series(['ddd','ccc','eee'], index=['x','y','z'])
# print(s3)

# 序列加入DataFrame
ss1 = pd.Series([1,2,3], index=[1,2,3], name='A')
ss2 = pd.Series([10,20,30], index=[1,2,3], name='B')
ss3 = pd.Series([100,200,300], index=[1,2,3], name='C')
ss4 = pd.Series([1000,2000,3000], index=[2,3,4], name='D')
ssd = {ss1.name:ss1, ss2.name:ss2, ss3.name:ss3}
ssl = [ss1,ss2, ss3]
df = pd.DataFrame(ssd) # name是列名，index是行号
df2 = pd.DataFrame(ssl) # index 是列名，name 是行号
# print(df)
# print(df2)
ssd[ss4.name] = ss4  #结果是合集，没有的显示NaN
df3 = pd.DataFrame(ssd)
print(df3)