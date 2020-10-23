n=eval(input("Nr natural="))
i=1; s=0; p=1
while(i<=n):
    s=s+i
    p=p*i
    i+=1
print(s,p,s/n)