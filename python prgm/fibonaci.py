a=0
b=1
n=int(input('enter any nber:'))
for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(c)