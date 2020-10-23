a1=0; a2=0; b1=0;b2=0; i=0
while i<12:
    i+=1
    x=eval(input())
    if(x<0):
        b1=b1+x
        b2+=1
    else:
        a1=a1+x
        a2+=1
print(round(a1/a2, 2), round(b1/b2, 2))