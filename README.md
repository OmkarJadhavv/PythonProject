from random import randint

play=['R', 'P', 'S']

computer = play[randint(0,2)]
count=0
total_count=5
player_points = 0
computer_points = 0
total_points = 5
while(count < total_count):
    player = input('\nMake your choice R, P OR S: ' )
    count = count + 1 
    if player==computer:
        print("\nTie")
    elif player== 'R':
        if computer == 'P':
            print("\nYou loose Paper covers Rock"  )
            computer_points = computer_points + 1 
            print("Computer Points= " + str(computer_points))
       
        else:
            print('\nYou win...! Rock smashes Scissor')
            player_points = player_points + 1
            print("Player Points= " + str(player_points))

    elif player == 'P':
        if computer== 'R':
            print('\nYou win...! Paper covers Rock')
            player_points = player_points + 1
            print("Player Points= " + str(player_points))
        
        else:
            print('\nYou Loose Scissor cuts Paper')
            computer_points = computer_points + 1
            print("Computer Points= " + str(computer_points))

    elif player=='S':
        if computer=='P':
            print('\nYou Win...! Scissor cuts Paper')
            player_points = player_points + 1
            print("Player Points= " + str(player_points))
        
        else:
            print('\nYou Loose Rock smashes Scissor')
            computer_points = computer_points + 1
            print("Computer Points= " + str(computer_points))

    else:
        print('\nInvalid move')

    if(count==total_count):
        if player_points > computer_points:
            print('\nPlayer has won the game\n')

        elif player_points == computer_points:
            print('\nThe game has tied\n')

        else:
            print('\nComputer has won the game\n')
    
    computer = play[randint(0,2)]
