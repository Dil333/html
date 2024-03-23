import random
user_score=0
comp_score=0
user_choice=int(input("enter number:"))
if(user_choice>=35):
    if user_choice==1:
       user_score+=user_choice
    else:
       user_score+=user_choice
print("user choice:",user_choice) 
print("now computer turn..")
comp_choice=random.randint(1,7)
if (user_choice==comp_choice):
    print("draw",end="")
    if comp_choice==1:
            comp_score+=comp_choice
            print("comp_choice:",comp_choice)
            print(user_choice,"vs",comp_choice)
    else:
            comp_score+=comp_choice
print("\nuser_score:",user_score,"\ncomp_score:",comp_score)
