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
   if n < 2:
       return n
   else:
       return(fibs(n-1) + fibs(n-2))

def run(items):
  for i in range(items):
    print(fibs(i))          #生成一组数列

#或者生成第n个斐波那契数列

def fibs(n):
    a = [0, 1]
    if n < 2:
        return a[n]
    else:
        for i in range(2, n+1):
            a.append(a[i-2]+a[i-1])
        return a[n]                 #生成第n个菲波那切数


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

#迭代器生成斐波那契数列    
 class Fab(object): 

    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
        
    def __iter__(self): 
        return self 
