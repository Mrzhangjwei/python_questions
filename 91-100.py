# -*- coding: cp936 -*-
#95.ʱ�亯����һ��������Ϸ���ж�һ���˷�Ӧ����
'''
import random
import time
guess=range(10)
person=input('>>>')
computer=random.choice(guess)
if person==computer:
    print "�¶���:",time.mktime(time.localtime())
while person>computer:
    print "�´���",time.mktime(time.localtime())
    person=input('>>>')
    if person==computer:
        print time.mktime(time.localtime())
        break
while person<computer:
    print "��С��",time.mktime(time.localtime())
    person=input('>>>')
    if person==computer:
        print time.mktime(time.localtime())
        break
'''
#96.�����ַ������Ӵ����ֵĴ���
'''
s='abchfjkdhgtuiabchgf1256abchii'
sub='abc'
print s.count(sub)
'''
#97.�Ӽ�������һЩ�ַ�������������͵�������ȥ��ֱ������һ��#Ϊֹ

#98.�Ӽ�������һ���ַ�������Сд��ĸȫ��ת��Ϊ��д��ĸ��Ȼ�������һ�������ļ���test���б��棬������ַ��ԣ�����
'''
s='dhsjkfhsi'
print s.swapcase()
f=open('�ĵ�(E):\������ѵPPT\Python�⼰��\test','w')
f.write(s.swapcase())
f.close()
'''
#99.�����������ļ�A��B�������һ����ĸ��Ҫ����������ļ��е���Ϣ�ϲ�������ĸ˳�����У��������һ�����ļ�C��
'''
A=['f','j','r','k','o','e','J','i','o','i']
B=[1,2,'h','f','V','d','A','f','h','j',3,'@','d']
C=A+B
C.sort()
print C
'''
