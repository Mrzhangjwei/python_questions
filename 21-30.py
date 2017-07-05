    # -*- coding: cp936 -*-
'''21.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，有第二天早上
又将上桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半多一个。到第十天早上想在吃，
见只剩下一个桃子了。求第一天共摘了多少。'''

'''22.两个乒乓队进行比赛，各出三人。甲队a,b,c三人，乙队x,y,z三人，一直抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编写程序找出三队三手的名单'''
'''
l1=['a','b','c']
l2=['x','y','z']
s1=zip("aaabbbccc",'xyz'*3)
print s1
s1.remove(('a','x'))
s1.remove(('c','x'))
s1.remove(('c','z'))
print s1
'''
#23.打印菱形图案
'''
s='  *  '
s1=' * * '
s2='*   *'
for i in range(5):
    if i==0 or i==4:
        print s.center(30)
    elif i==1 or i==3:
        print s1.center(30)
    else:
        print s2.center(30)
'''
#24.求2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的前20项之和
'''
l=[2,3]
l1=[1,2]
l2=[]
sum=0
def febo(N):
    for i in range(N-2):
        l.append(float(l[-2]+l[-1]))
    print l  
def febo1(N):
    for i in range(N-2):
        l1.append(float(l1[-2]+l1[-1]))
    print l1    
febo(20)
febo1(20)
for i in range(20):
    for j in range(20):
        if i==j:
            l2.append(l[i]/l1[j])
print l2
for i in range(20):
    sum+=l2[i]
print sum
'''
#25.求1！+2！+3！+4！+...+20！之和
'''
sum=1
sum1=1
sum2=1
sum3=1
sum4=1
sum5=1
sum6=1
sum7=1
sum8=1
sum9=1
sum10=1
sum11=1
sum12=1
sum13=1
sum14=1
sum15=1
sum16=1
sum17=1
sum18=1
sum19=1
for i in range(20,0,-1):
    sum*=i
for i in range(19,0,-1):
    sum1*=i
for i in range(18,0,-1):
    sum2*=i
for i in range(17,0,-1):
    sum3*=i
for i in range(16,0,-1):
    sum4*=i
for i in range(15,0,-1):
    sum5*=i
for i in range(14,0,-1):
    sum6*=i
for i in range(13,0,-1):
    sum7*=i
for i in range(12,0,-1):
    sum8*=i
for i in range(11,0,-1):
    sum9*=i
for i in range(10,0,-1):
    sum10*=i
for i in range(9,0,-1):
    sum11*=i
for i in range(8,0,-1):
    sum12*=i
for i in range(7,0,-1):
    sum13*=i
for i in range(6,0,-1):
    sum14*=i
for i in range(5,0,-1):
    sum15*=i
for i in range(4,0,-1):
    sum16*=i
for i in range(3,0,-1):
    sum17*=i
for i in range(2,0,-1):
    sum18*=i
for i in range(1,0,-1):
    sum19*=i
sum20=sum+sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8+sum9+sum10+sum11+sum12+sum13+sum14+sum15+sum16+sum17+sum18+sum19
print sum20
'''
#26.使用递归方法求5！
'''
def func(N):
    if N==0:
        return 1
    else:
        return N*func(N-1)
print func(5)
'''
#27.利用递归函数调用方式，将所输入的5个字符，以相反的顺序打印出来

'''28.有5个人坐在一起，问第五个人多少岁。他说比第四个人大2岁。问第四个人岁数，他说比第三个人大2岁。
问第三个人，又说比第二个人大2岁。问第二个人，又说比第一个人大2岁。最后问第一个人，他说是10岁'''
'''
def func(N):
    for i in range(N):
        a=10+2*i
    print a
func(5)
'''
#29.给一个不多于5位数的正整数，输入它有几位数，并逆序打印出各位数字
'''
i=input("请输入数字:"+'>>>')
a=i/10000
b=i%10000/1000
c=i%1000/100
d=i%1000%100/10
e=i%10
s=a*10000+b*1000+c*100+d*10+e
if a!=0:
    print "它有五位数字"
    print e,d,c,b,a
else:
    if b!=0:
        print "它有四位数字"
        print e,d,c,b,0 else:
        if c!=0:
            print "它有三位数字"
            print e,d,c,0,0
        else:
            if d!=0:
                print "它有两位数字"
                print e,d,0,0,0
            else:
                print "它有一位数字"
                print e,0,0,0,0
'''
#30.一个五位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
'''
for i in range(10000,99999):
    a=i/10000
    b=i%10000/1000
    c=i%1000/100
    d=i%1000%100/10
    e=i%10
    i==a*10000+b*1000+c*100+d*10+e
    if a==e and b==d :
        print i,
'''
