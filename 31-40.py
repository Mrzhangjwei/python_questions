# -*- coding: cp936 -*-
#31.���������ڼ��ĵ�һ����ĸ���ж�һ�������ڼ��������һ����ĸһ����������жϵڶ�����ĸ
'''
a=raw_input('>>>')
if a=='M':
    print "������һ:'Monday'"
elif a=='T':
    print "��������ܶ���Ҳ����������"
    b=raw_input('>>>')
    if b=='u':
        print "�����ܶ�:'Tuesday'"
    elif b=='h':
        print "��������:'Thursday'"
elif a=='W':
    print "��������:'Wednesday'
elif a=='F':
    print "��������:'Friday'"
elif a=='S':
    print "�������������Ҳ����������"
    c=raw_input('>>>')
    if c=='a':
        print "��������:'Saturday'"
    elif c=='u':
        print "��������:'Funday'"
else :
    print "δ֪����"
'''
#36.��100֮�ڵ�����
'''
l=[]
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            if i==99:
                break
            else:
                i+=1 
        else:
            if j==i:
                break
            else: 
                if i%j!=0:
                    j+=1
                    if j==i:
                        l.append(j)
l.insert(0,2)
print l
'''
#37.��10������������
'''
l=[1,24,3,65,46,35,24,7,54,45]
l.sort()
print l
l.sort(reverse=True)
print l
'''
#38.��һ��3*3����Խ���֮��

#39.��һ���Ѿ��ź�������顣������һ������Ҫ��ԭ���Ĺ��ɽ�������������

#40.��һ�������������

