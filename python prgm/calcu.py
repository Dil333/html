a=int(input('enter first nmber:'))
b=int(input('enetr second number:'))
print('1.addition\n2.substraction\n3.multiplication\n4.divisiion')           
option=int(input('enter your choice:'))
if option==1:
    result=a+b
    print('the addition is',result)
elif option==2:
    print('the substraction is',a-b)
elif option==3:
    print('the multiplication is',a*b)
elif option==4:
    print('the division is',a/b)
else:
    print('invalid choice')


