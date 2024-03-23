import random
car_count=0
goat_count=0
for i in range(1,10):
        doors=["goat","car","goat"]
        choose=random.sample(doors,3)
        select=int(input('1.doorA\n2.doorB\n3.doorC\nenter your choice:'))
        if select==1:
            print('you got',choose[0])
        elif select==2:
            print('you got',choose[1])
        elif select==3:
            print('you got',choose[2])
        if choose[select-1]=='car':
            car_count+=1
        else:
            goat_count+=1
print('goat_count:',goat_count,'\ncar_count:',car_count)
            