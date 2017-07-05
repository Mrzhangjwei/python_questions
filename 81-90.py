# -*- coding: cp936 -*-
#83.求0-7所能组成的奇数个数
'''
l=[]
for i in range(8):
    if i%2!=0:
        l.append(i)
print len(l)
'''
#84.一个偶数总能表示两个素数之和
'''
import random
l=[]
for i in range(101,201):
    for j in range(2,i):
        if i%j==0:
            i+=1
        else:
            if i%j!=0:
                j+=1
                if j==i:
                    l.append(j)
l1=random.sample(l,2)
s=l1[0]+l1[1]
print l1[0],l1[1]
if s%2==0:
    print s
'''
#85.判定一个素数能被几个9整除

#86.将两个字符串进行连接
'''
s1='fhdjk'
s2='ffhuidh'
s3='1567'
print s1+s2
print s1.join(s3)
print s1*2
'''
#88.读取7个数（1-50）的整数值，每读取一个值，程序打印出该值个数的*
'''
import random
l=random.sample(range(1,51),7)
for i in range(len(l)):
    print '*'*l[i]
'''
#89.某公司采用公用电话传递数据，数据是四位数，在传递过程中是加密的
#每位数字都加上5，然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
'''
if __name__=='__main__':
    M=5
    a=[1,2,3,4,5]
    i=0
    j=M-1
    while i<M:
        a[i],a[j]=a[j],a[i]
        print a
        i+=1
        j-=1
    for i in range(5):
        print a[i]
'''
