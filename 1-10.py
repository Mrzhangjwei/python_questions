# -*- coding: cp936 -*-
#1.有1,2,3,4个数字，能组成多少个互不相同且无重复数字的三位数
'''
import random
l=[1,2,3,4]
m=[]
for i in l:
    a1=random.choice(l)
    a2=random.choice(l)
    if a1!=i and a2!=i and a1!=a2 :
        m.append(i*100+a1*10+a2)
        m.append(i*100+a2*10+a1)
        m.append(a1*100+i*10+a2)
        m.append(a1*100+a2*10+i)
        m.append(a2*100+i*10+a1)
        m.append(a2*100+a1*10+i)
print len(m)
'''

'''2.企业发放的奖金根据利润提成，利润I：
低于或等于10万元时，奖金可提10%；
高于10万元，低于20万元时，高于10万元的部分，可提成7.5%
20万元到40万元之间时，高于20万元的部分，可提成5%
40万元到60万元之间时，高于40万元的部分，可提成3%
60万元到100万元之间时，高于60万元的部分，可提成1.5%
高于100万时，超过100万元的部分按1%提成
从键盘输入当月利润I，求应发奖金总数
'''
"""
I=input('>>>')
if I<10**6:
    if I<=10**5:
        w1=I*0.10
        print w1
    elif I>100000 and I<=200000 :
        w2=(I-100000)*0.075+100000*0.10
        print w2
    elif I>200000 and i<=400000 :
        w3=(I-200000)*0.05+200000*0.075
        print w3
    elif I>400000 and i<=600000 :
        w4=(I-400000)*0.03+400000*0.05
        print w4
    elif I>600000 and I<=10**6:
        w5=(I-600000)*0.015+600000*0.03
        print w5
else :
    w6=(I-1000000)*0.01+1000000*0.015
    print w6
"""
#3.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，问该数是多少？
'''
from math import sqrt
for i in range(100):
    m=sqrt(100+i)
    n=sqrt(268+i)
    if (m*m==100+i) and (n*n==268+i):
        print i,
'''
#4.输入某年某月某日，判断这一天是这一年的第几天
'''
import time
a=time.localtime()
print a[-2]
print a.tm_yday
'''
#5.任意输入三个整数x，y，z，请把这三个数有小到大的顺序输
'''
x=input('>>>')
y=input('>>>')
z=input('>>>')
l=[]
l.extend([x,y,z])
l.sort()
print l
'''
#6.用*输出字母C的图案
'''
a=input('>>>')
l=' * * *'
for i in range(1,a+1):
    if i==1 or i==a:
        print l
    else:
        print '*'
'''
#7.输出图案，看一看Very Beautiful
'''
s='very beautiful'
print s.title()
'''
#8.输出9*9乘法口诀
'''
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print '%s*%s=%s'%(j,i,j*i),
    print '\n'

for i in range(9,0,-1):
    for j in range(1,10):
        if j<=i:
            print '%s*%s=%s'%(j,i,j*i),
    print '\n'
'''
#9.输出国际象棋棋盘
'''
import wx
app=wx.App()
win=wx.Frame(None,title='国际象棋棋盘')
panel=wx.Panel(win)
bt=[]
for i in range(1,17):
    bt.append(wx.Button(panel))
s_box=wx.BoxSizer()
s_box.Add(bt[0],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s_box.Add(bt[1],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s_box.Add(bt[2],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s_box.Add(bt[3],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

s1_box=wx.BoxSizer()
s1_box.Add(bt[4],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s1_box.Add(bt[5],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s1_box.Add(bt[6],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s1_box.Add(bt[7],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

s2_box=wx.BoxSizer()
s2_box.Add(bt[8],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s2_box.Add(bt[9],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s2_box.Add(bt[10],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s2_box.Add(bt[11],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

s3_box=wx.BoxSizer()
s3_box.Add(bt[12],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s3_box.Add(bt[13],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s3_box.Add(bt[14],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s3_box.Add(bt[15],proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

v_box=wx.BoxSizer(wx.VERTICAL)
v_box.Add(s_box,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
v_box.Add(s1_box,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
v_box.Add(s2_box,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
v_box.Add(s3_box,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

panel.SetSizer(v_box)
win.Show()
app.MainLoop()
'''
#10.打印楼梯，同时在楼梯上放打印一个笑脸
'''
a=input('>>>')
for i in range(a+1,0,-1):
    if i==a+1:
        print '\t@'.expandtabs(a+4)
    else:
        print "\t*****".expandtabs(i)
'''










        
    
