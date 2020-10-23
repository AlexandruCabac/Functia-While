s=0; i=1
while i!=0:
    a=eval(input())
    if a%2==0:
        s=s+a
    elif(a%2==1 and a%3==0):
        i=0
else:
    print(s)