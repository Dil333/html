print("welcome to our uize competetion...")
answer=input("would you like to play,ifso,(y/n):")
score=0
total_question=3
if answer=='yes':
    print("1.which country has largest population in the world?")
    answer=int(input("1.china\n2.india\n3.canada\n4.america\nchoice:"))
    if answer==2:
        score+=1
        print('correct')
    else:
        print('wrong')
    print('2.which country has highest mountain avarest in the world?')
    answer=int(input("1.nepal\n2.bhutan\n3.india\n4.pakistan\nchoice:"))
    if answer==1:
        score+=1
        print("correct")
    else:
        print("wrong")
    print('3.which is the smaller bird in the world?')
    answer=int(input("1.bat\n2.ostrich\n3.homingbird\n4.parote\nchoice:"))
    if answer==3:
        score+=1
        print("correct")
    else:
        print("wrong")
else:
    print("end....")
print("thanks for playing game,attemped,",score,"question correctly!")
mark=(score/total_question)*100
print("mark obtained:",mark)
dil=input("do you want to play again(y/n)")