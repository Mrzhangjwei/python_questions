#兔子问题
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
#求101-200之间的质数
'''
from math import sqrt 
def main():
    for i in range(1,201):
        flag = 1
        k = int(sqrt(i))
        for j in range(2,k+1):
            if i%j == 0:
                flag = 0
                break
        if flag == 1:
            print '%3d'%(i),
    
if __name__ == "__main__":
    main()
'''
#水仙花数
'''
def main():
    for i in range(100,1000):
        a = i%10
        b = i/100
        c = (int(i/10))%10
        if i == a**3+b**3+c**3:
            print "%5d"%(i),

if __name__ == "__main__":
    main()
'''
'''
print 3**2
print 3**4
'''
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
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
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
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
#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
'''
def main():
    basis = int(raw_input("Input the basis number:"))
    n = int(raw_input("Input the longest length of number:"))
    b = basis
    sum = 0
    for i in range(0,n):
        if i==n-1:
            print "%d "%(basis),
        else:
            print "%d +"%(basis),
        sum+=basis
        basis = basis*10+b
    print '= %d'%(sum),
    

if __name__ == '__main__':
    main()
'''
'''
【程序38】
题目：求一个3*3矩阵对角线元素之和 
'''
'''
l = []
for i in range(3):
    for j in range(3):
        l.append(int(raw_input('Input a number:')))
s = 0
for i in range(3):
    s += l[3*i+i]
print s
'''
'''
【程序39】
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''
'''
l = [0,10,20,30,40,50]

print 'The sorted list is:',l
cnt = len(l)
n = int(raw_input('Input a number:'))
l.append(n)
for i in range(cnt):
    if n<l[i]:
        for j in range(cnt,i,-1):
            l[j] = l[j-1]
        l[i] = n
        break
print 'The new sorted list is:',l
'''
'''
【程序54】
题目：取一个整数a从右端开始的4～7位。
'''
'''
a = 100
print 100&0x00F0
'''
'''
【程序56】
题目：画圆【Tkinter模块】
'''
'''
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg='red')  
    canvas.pack(expand=YES, fill=BOTH)                
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3

    mainloop()
'''
'''
【程序57】
题目：画直线。
1.程序分析：　　　　　　　　　　　
2.程序源代码： 
'''
'''
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')   
    canvas.pack(expand=YES, fill=BOTH)                  
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0,y0,x0,y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0,y0,x0,y1,fill = 'red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()
'''


