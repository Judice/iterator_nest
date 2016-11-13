# coding=utf-8
mylist = [x*x for x in range(3)] #迭代器
for i in mylist:
    print i

mygenerator = (x*x for x in range(3)) #生成器, []变为()
for i in mygenerator:
    print i

def createGenarator():  #yield的使用,创建生成器
    for i in range(3):
        yield i*i

mygenerator = createGenarator() #创建生成器实例
for i in mygenerator:
    print i