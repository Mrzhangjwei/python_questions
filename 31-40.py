# -*- coding: cp936 -*-
#31.请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
'''
a=raw_input('>>>')
if a=='M':
    print "这是周一:'Monday'"
elif a=='T':
    print "这可能是周二，也可能是周四"
    b=raw_input('>>>')
    if b=='u':
        print "这是周二:'Tuesday'"
    elif b=='h':
        print "这是周四:'Thursday'"
elif a=='W':
    print "这是周三:'Wednesday'
elif a=='F':
    print "这是周五:'Friday'"
elif a=='S':
    print "这可能是周六，也可能是周日"
    c=raw_input('>>>')
    if c=='a':
        print "这是周六:'Saturday'"
    elif c=='u':
        print "这是周日:'Funday'"
else :
    print "未知错误"
'''
#36.求100之内的素数
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
#37.对10个数进行排序
'''
l=[1,24,3,65,46,35,24,7,54,45]
l.sort()
print l
l.sort(reverse=True)
print l
'''
#38.求一个3*3矩阵对角线之和

#39.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插如数组中

#40.将一个数组逆序输出

