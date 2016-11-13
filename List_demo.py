# coding=utf-8
mylist = [x*x for x in range(3)] #迭代器
for i in mylist:
    print i

mygenerator = (x*x for x in range(3)) #生成器, []变为()
for i in mygenerator:
    print i