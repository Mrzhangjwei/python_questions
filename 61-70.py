# -*- coding: cp936 -*-
#61.打印杨辉三角形（要求打印5行）
'''
l1=[1]
l2=[1,1]
l3=[1]
l4=[1]
l5=[1]
def func():
    print str(l1).center(50)
    print str(l2).center(50)
    for i in range(len(l2)):
        if i==len(l2)-1:
            break
        l3.append(l2[i]+l2[i+1])
    l3.append(1)
    print str(l3).center(50)
    for i in range(len(l3)):
        if i==len(l3)-1:
            break
        l4.append(l3[i]+l3[i+1])
    l4.append(1)
    print str(l4).center(50)
    for i in range(len(l4)):
        if i==len(l4)-1:
            break
        l5.append(l4[i]+l4[i+1])
    l5.append(1)
    print str(l5).center(50)
func()
'''
#66.输出3个数a,b,c，按大小顺序输出
a=input('请输入第一个数：'+'>>>')
b=input('请输入第二个数：'+'>>>')
c=input('请输入第三个数：'+'>>>')
if a>b:
    
#67.输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
'''
l=['a','f',1,4,'@','A']
l.sort()
print l
t=l[-1]
l[-1]=l[0]
l[0]=t
print l
'''
#68.有n个整数，使其前面各个顺序向后移动m个位置，最后m个数变成最前面的m个数

#69.有n个人围成一圈，顺序排号。从第一个人开始报数（从1报道3），繁报道3的人退出圈子，问最后留下的是原来的第几号

#70.写一个函数，求一个字符串的长度，在main()函数中输入字符串，并输出其长度
'''
def func():
    s=raw_input('>>>')
    print len(s)
func()
'''
