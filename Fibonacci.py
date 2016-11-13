# coding=utf-8
"""
    斐波那契数列
"""

#for循环生成斐波那契数列
def fibs(n):
    a, b = 0, 1
    for i in range(0,n):
        f = a
        a, b =b, a+b
        print f


#递归函数生成斐波那契数列
def fibs(n):
   if n <= 1:
       return n
   else:
       return(fibs(n-1) + fibs(n-2))

def run(items):
  for i in range(items):
    print(fibs(i))


#迭代器生成斐波那契数列
class Fibs():
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        f = self.a
        self.a, self.b = self.b, self.a+self.b
        return f

    def __iter__(self):
        return self
