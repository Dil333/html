import random
user_score=0
com_score=0
dil=input('do you want to play(yes/no):')
if dil=='yes':
    print('\nWELECOME TO OUR GAME....\n\n')
    while True:
        print('you can see overhere....\n1.rock\n2.paper\n3.scissor\n*.exit')
        choice=int(input('enter your choice:'))
        if choice==1:
            choice_name='rock'
        elif choice==2:
            choice_name='paper'
        elif choice==3:
            choice_name='scissor'
        else:
            break
        print('the user choice is',choice_name)
        print('now computer turn....')
        com_choice=random.randint(1,3)
        if com_choice==1:
            com_choice_name='rock'
        elif com_choice==2:
            com_choice_name='paper'
        else:
            com_choice_name='scissor'
        print('the computer choice is',com_choice_name)
        print(choice_name,'vs',com_choice_name)
        if choice==com_choice:
            print('it is draw',end="")
            result='draw'
        elif (choice==1 and com_choice==2):
            print('paper win')
            com_score+=1
        elif(com_choice==3 and choice==1):
            print('rock win')
            user_score+=1
        elif(choice==2 and com_choice==3):
            print('scissor win')
            com_score+=1
        elif(choice==2 and com_choice==1):
            print('paper win')
            user_score+=1
        elif(choice==3 and com_choice==1):
            print('rock win')
            com_score+=1
        elif(choice==3 and com_choice==2):
            print('scissor win')
            user_score+=1
        else:
            print('error')
    print('score of user:',user_score,'\nscore of computer:',com_score)
else:
    print("end....",end="")