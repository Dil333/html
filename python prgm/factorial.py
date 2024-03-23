def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
num=int(input("enter any number:"))
result=fact(num)
print('the factorial num is:',num,'=',result)