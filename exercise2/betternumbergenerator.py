from random import randint
def weightedrandom(a,b):
    numberlist=[]
    for i in range (a,b+1):
        numberlist.append(i)
    x=randint(600,1000)/1000
    e=(b+1)*x
    c=round(e)
    for j in range(c,b+1):
        numberlist.append(j)
    L=len(numberlist)
    y=randint(0,L-1)
    finalnumber=numberlist[y]
    return finalnumber


    

