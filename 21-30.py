    # -*- coding: cp936 -*-
'''21.���ӳ������⣺���ӵ�һ��ժ�����ɸ����ӣ���������һ�룬������񫣬�еڶ�������
�ֽ������ӳԵ�һ�룬�ֶ����һ�����Ժ�ÿ�����϶�����ǰһ��ʣ�µ�һ���һ��������ʮ���������ڳԣ�
��ֻʣ��һ�������ˡ����һ�칲ժ�˶��١�'''

'''22.����ƹ�Ҷӽ��б������������ˡ��׶�a,b,c���ˣ��Ҷ�x,y,z���ˣ�һֱ��ǩ��������������
�������Ա����������������a˵������x�ȣ�c˵������x,z�ȣ����д�����ҳ��������ֵ�����'''
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
#23.��ӡ����ͼ��
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
#24.��2/1,3/2,5/3,8/5,13/8,21/13...���������е�ǰ20��֮��
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
#25.��1��+2��+3��+4��+...+20��֮��
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
#26.ʹ�õݹ鷽����5��
'''
def func(N):
    if N==0:
        return 1
    else:
        return N*func(N-1)
print func(5)
'''
#27.���õݹ麯�����÷�ʽ�����������5���ַ������෴��˳���ӡ����

'''28.��5��������һ���ʵ�����˶����ꡣ��˵�ȵ��ĸ��˴�2�ꡣ�ʵ��ĸ�����������˵�ȵ������˴�2�ꡣ
�ʵ������ˣ���˵�ȵڶ����˴�2�ꡣ�ʵڶ����ˣ���˵�ȵ�һ���˴�2�ꡣ����ʵ�һ���ˣ���˵��10��'''
'''
def func(N):
    for i in range(N):
        a=10+2*i
    print a
func(5)
'''
#29.��һ��������5λ�������������������м�λ�����������ӡ����λ����
'''
i=input("����������:"+'>>>')
a=i/10000
b=i%10000/1000
c=i%1000/100
d=i%1000%100/10
e=i%10
s=a*10000+b*1000+c*100+d*10+e
if a!=0:
    print "������λ����"
    print e,d,c,b,a
else:
    if b!=0:
        print "������λ����"
        print e,d,c,b,0 else:
        if c!=0:
            print "������λ����"
            print e,d,c,0,0
        else:
            if d!=0:
                print "������λ����"
                print e,d,0,0,0
            else:
                print "����һλ����"
                print e,0,0,0,0
'''
#30.һ����λ�����ж����ǲ��ǻ���������12321�ǻ���������λ����λ��ͬ��ʮλ��ǧλ��ͬ
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
