list = []
for i in range(1,21):
    list.append(i)
print(list)

#1格式1：结果 for 变量 in 可迭代；变量等于结果
list = [i for i in range(1,21)]
print(list)

list1 = [i + 2 for i in range(1,21)]
print(list1)

# 1-100 偶数
list2 = [i for i in range(0,100,2)]
print(list2)

#格式2：结果 for 变量 in 可迭代 if 变量得出结果
list3 = [i for i in range(0,100) if i%2==0] # 先执行for 循环然后再执行if，最后赋值到i
print(list3)

list4 = ['62','hello','100','world','luck','88','high']
list5 = [w for w in list4 if w.isalpha()] # 取出列表中所有字母的元素
print(list5)

#格式3：结果1 if 调节 else 结果2 for 变量 in 可迭代；变量得出后做判断

# h 单词首字母大写，其它的单词都大写
list6 = [w.title() if w.startswith('h') else w.upper() for w in list4] # 循环遍历出的结果
print(list6)

# 双层选混
list7 = []
for i in range(1,3):
    for j in range(1,3):
        list7.append((i,j))
print(list7)

list7 = [(i,j) for i in range(1,3) for j in range(1,3)]
print(list7)