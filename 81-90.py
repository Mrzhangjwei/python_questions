# -*- coding: cp936 -*-
#83.��0-7������ɵ���������
'''
l=[]
for i in range(8):
    if i%2!=0:
        l.append(i)
print len(l)
'''
#84.һ��ż�����ܱ�ʾ��������֮��
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
#85.�ж�һ�������ܱ�����9����

#86.�������ַ�����������
'''
s1='fhdjk'
s2='ffhuidh'
s3='1567'
print s1+s2
print s1.join(s3)
print s1*2
'''
#88.��ȡ7������1-50��������ֵ��ÿ��ȡһ��ֵ�������ӡ����ֵ������*
'''
import random
l=random.sample(range(1,51),7)
for i in range(len(l)):
    print '*'*l[i]
'''
#89.ĳ��˾���ù��õ绰�������ݣ���������λ�����ڴ��ݹ������Ǽ��ܵ�
#ÿλ���ֶ�����5��Ȼ���úͳ���10��������������֣��ٽ���һλ�͵���λ�������ڶ�λ�͵���λ����
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
