# -*- coding: cp936 -*-
#11.古典问题，有一对兔子，从出生后第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生出一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
n = input('输入数字\n>>>')
def tuzi(n):
      a = 1
      b = 1
      for i in range(1,n+1,2):
          print '%d %d'%(a,b),
          a += b
          b += a
tuzi(n)
'''
#12.判断101-200之间有多少个素数，并输出所有素数
'''
l=[]
for i in range(101,201):
    for j in range(2,i):
        if i%j==0:
            i+=1
            continue
        else:
            if i%j!=0:
                j+=1
                if j==i:
                    l.append(j)
print l
'''
#13.打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。如：153=1*1*1*1+5*5*5+3*3*3
'''
for i in range(500):
    x=i/100
    y=i%100/10
    z=i%10
    if i==x**3+y**3+z**3:
        print i,
'''
#14.将一个正整数分解质因数，如：输入90，打印出90=2*3*3*5
'''
def main():
    n = int(raw_input('Enter a number:'))
    print n,'=',
    while(n!=1):
        for i in range(2,n+1):
            if (n%i)==0:
                n/=i
                if(n == 1):
                    print '%d'%(i)
                else:
                    print '%d *'%(i),
                break
            
        
if __name__ == "__main__":
    main()
'''
#15.利用条件运算符的嵌套来完成此题：学生成绩>90分的同学用A表示，60-89分之间的用B表示，60分以下的用C来表示
'''
a=input('>>>')
if a<=90:
    if a>=60 and a<=89 :
        print 'B'
    else:
        print 'C'
else :
    print 'A'
'''
#17.输入一行字符，分别统计出其中英文字母，空格，数字和其它字符的个数
'''
import re
s="13' '24' ''z''a''m''y''\t''\n'6'\r''$''@''A''H''*'"
shuzi=re.findall(r'\d',s)
print len(shuzi)
zimu=re.findall(r'[A-Za-z]',s)
print len(zimu)
kongge=re.findall(r' ',s)
print len(kongge)
teshu=re.findall(r'[\f|\n|\r|\t|\v|$|%|*|@]',s)
print len(teshu)
'''

'''
import string
def main():
    s = raw_input('input a string:')
    letter = 0
    space = 0
    digit = 0
    other = 0
    for c in s:
        if c.isalpha():
            letter+=1
        elif c.isspace():
            space+=1
        elif c.isdigit():
            digit+=1
        else:
            other+=1
    print 'There are %d letters,%d spaces,%d digits and %d other characters in your string.'%(letter,space,digit,other)

if __name__ == '__main__':
    main()
'''
#18.求s=a+aa+aaa+aaaa+aa..a的值，其中a是一个数字。例如：2+22+222（此时公有3个数相加），几个数有键盘控制。
'''
import random
a=input('>>>')
s=0
b=2
for i in range(1,a+1):
    s+=int(str(b)*i)
print s
'''
#19.一个数如果恰好等于它的因子之和，这个数称为“完数”，例如6=1+2+3，编写1000以内的所有完数


#20.一球从100米高度落下，每次落地后反弹回原来高度的一半；再落下，求它在第十次落地时，共经过多少米？第十次反弹多高？
'''
def High(num):
    if num/2.0 < 1:
        return 1
    else:
        return num+num/2.0+High(num/2.0)
print High(100)
'''
