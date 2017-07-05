l=[]
for i in range(2,100):
    for j in range(2,i):
        if i%j!=0:
            if j<i-1:
                j+=1
            else:
                l.append(i)
                break
        else:
            break
print l
            
