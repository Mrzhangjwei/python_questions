# -*- coding: cp936 -*-
#11.�ŵ����⣬��һ�����ӣ��ӳ��������������ÿ���¶���һ�����ӣ�С���ӳ����������º�ÿ����������һ�����ӣ��������Ӷ���������ÿ���µ���������Ϊ���٣�
'''
n = input('��������\n>>>')
def tuzi(n):
      a = 1
      b = 1
      for i in range(1,n+1,2):
          print '%d %d'%(a,b),
          a += b
          b += a
tuzi(n)
'''
#12.�ж�101-200֮���ж��ٸ��������������������
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
#13.��ӡ�����еġ�ˮ�ɻ���������ν��ˮ�ɻ�������ָһ����λ�������λ���������͵��ڸ��������磺153=1*1*1*1+5*5*5+3*3*3
'''
for i in range(500):
    x=i/100
    y=i%100/10
    z=i%10
    if i==x**3+y**3+z**3:
        print i,
'''
#14.��һ���������ֽ����������磺����90����ӡ��90=2*3*3*5
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
#15.���������������Ƕ������ɴ��⣺ѧ���ɼ�>90�ֵ�ͬѧ��A��ʾ��60-89��֮�����B��ʾ��60�����µ���C����ʾ
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
#17.����һ���ַ����ֱ�ͳ�Ƴ�����Ӣ����ĸ���ո����ֺ������ַ��ĸ���
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
#18.��s=a+aa+aaa+aaaa+aa..a��ֵ������a��һ�����֡����磺2+22+222����ʱ����3������ӣ����������м��̿��ơ�
'''
import random
a=input('>>>')
s=0
b=2
for i in range(1,a+1):
    s+=int(str(b)*i)
print s
'''
#19.һ�������ǡ�õ�����������֮�ͣ��������Ϊ��������������6=1+2+3����д1000���ڵ���������


#20.һ���100�׸߶����£�ÿ����غ󷴵���ԭ���߶ȵ�һ�룻�����£������ڵ�ʮ�����ʱ�������������ף���ʮ�η�����ߣ�
'''
def High(num):
    if num/2.0 < 1:
        return 1
    else:
        return num+num/2.0+High(num/2.0)
print High(100)
'''
