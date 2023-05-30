import random
l=["rock", "paper", "scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start.....    
1 Yes
2 No | Exit

        '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Paper
3 Scissor
'''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="paper"
            elif userInput==3:
                uchoice="scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value", Cchoice)
                print("User value", uchoice)
                print("Game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer value", Cchoice)
                print("User value", uchoice)
                print("You win") 
                ucount=ucount+1
            else:
                print("Computer value", Cchoice)
                print("User value", uchoice)
                print("Computer win")
                ccount=ccount+1

        if ucount==ccount:
            print("Final Game Draw...")
            print("User score", ucount)
            print("Computer score", ccount)
        elif ucount>ccount:
            print("You Win the Game...")
            print("User score", ucount)
            print("Computer score", ccount)
        else:
            print("Computer Win the Game...")
            print("User score", ucount)
            print("Computer score", ccount)    



    else:
        break                                                     
    
