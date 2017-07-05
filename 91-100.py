# -*- coding: cp936 -*-
#95.时间函数：一个猜字游戏，判断一个人反应快慢
'''
import random
import time
guess=range(10)
person=input('>>>')
computer=random.choice(guess)
if person==computer:
    print "猜对了:",time.mktime(time.localtime())
while person>computer:
    print "猜大了",time.mktime(time.localtime())
    person=input('>>>')
    if person==computer:
        print time.mktime(time.localtime())
        break
while person<computer:
    print "猜小了",time.mktime(time.localtime())
    person=input('>>>')
    if person==computer:
        print time.mktime(time.localtime())
        break
'''
#96.计算字符串中子串出现的次数
'''
s='abchfjkdhgtuiabchgf1256abchii'
sub='abc'
print s.count(sub)
'''
#97.从键盘输入一些字符，逐个把他们送到磁盘上去，直到输入一个#为止

#98.从键盘输入一个字符串，将小写字母全部转换为大写字母，然后输出到一个磁盘文件“test”中保存，输出的字符以！结束
'''
s='dhsjkfhsi'
print s.swapcase()
f=open('文档(E):\暑期培训PPT\Python题及答案\test','w')
f.write(s.swapcase())
f.close()
'''
#99.有两个磁盘文件A和B，各存放一行字母，要求把这两个文件中的信息合并（按字母顺序排列），输出到一个新文件C中
'''
A=['f','j','r','k','o','e','J','i','o','i']
B=[1,2,'h','f','V','d','A','f','h','j',3,'@','d']
C=A+B
C.sort()
print C
'''
