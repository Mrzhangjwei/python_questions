# -*- coding: cp936 -*-
#61.��ӡ��������Σ�Ҫ���ӡ5�У�
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
#66.���3����a,b,c������С˳�����
a=input('�������һ������'+'>>>')
b=input('������ڶ�������'+'>>>')
c=input('���������������'+'>>>')
if a>b:
    
#67.�������飬�������һ��Ԫ�ؽ�������С�������һ��Ԫ�ؽ������������
'''
l=['a','f',1,4,'@','A']
l.sort()
print l
t=l[-1]
l[-1]=l[0]
l[0]=t
print l
'''
#68.��n��������ʹ��ǰ�����˳������ƶ�m��λ�ã����m���������ǰ���m����

#69.��n����Χ��һȦ��˳���źš��ӵ�һ���˿�ʼ��������1����3����������3�����˳�Ȧ�ӣ���������µ���ԭ���ĵڼ���

#70.дһ����������һ���ַ����ĳ��ȣ���main()�����������ַ�����������䳤��
'''
def func():
    s=raw_input('>>>')
    print len(s)
func()
'''
