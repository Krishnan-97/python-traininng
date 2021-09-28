while True:
    p1 = input("Player1 Enter(rock,paper,scissor):")
    p2 = input("Player2 Enter(rock,paper,scissor):")

    if(p1 == 'rock'):
        if(p2 == 'paper'):
            print("Player2 wins!!")
        elif(p2 == 'scissor'):
            print('Player1 wins!!')
        elif(p2 == 'rock'):
            print('Draw!!')

    elif(p1 == 'paper'):
        if(p2 == 'paper'):
            print("Draw!!")
        elif(p2 == 'scissor'):
            print('Player2 wins!!')
        elif(p2 == 'rock'):
            print('Player1!!')

    elif(p1 == 'scissor'):
        if(p2 == 'paper'):
            print("Player1 wins!!")
        elif(p2 == 'scissor'):
            print('Draw!!')
        elif(p2 == 'rock'):
            print('Player2 wins!!')

    p = input("Do you want to play again??(y/n)")
    if(p == 'y'):
        continue
    else:
        break
