import random as rd
choices = ('Snake','water','gun')
player_choice = input('snake, water or gun')
comp_choice = rd.choice(choices)
def swg(player_choice, computer_choice):
   score = 0
   while True:
    player_choice = input('snake, water or gun')
    comp_choice = rd.choice(choices)
    if player_choice not in choices:
        print('Invalid choice')
        continue
    if score == 3:
        print('You win!')
        break
    if score < 0:
        print('You lose!')
        break
    if player_choice == computer_choice:
        print(f'the computer chose {player_choice} and the player chose {computer_choice}')
        print('it results in draw')
    elif player_choice == 'gun':
        if computer_choice == 'snake':
         print(f'the computer chose {player_choice} and the player chose {computer_choice}')
         print('you win ')
         score += 1
        else:
            print(f'the computer chose {player_choice} and the player chose {computer_choice}')
            print('you lose')
    elif player_choice == 'water':
        if computer_choice == 'gun':
                print(f'the computer chose {player_choice} and the player chose {computer_choice}')
                print('you lose ')
        else:
                print(f'the computer chose {player_choice} and the player chose {computer_choice}')
                print('you win')
                score += 1
    elif player_choice == 'snake':
        if computer_choice == 'water':
                print(f'the computer chose {player_choice} and the player chose {computer_choice}')
                print('you win ')
                score += 1
        else:
                print(f'the computer chose {player_choice} and the player chose {computer_choice}')
                print('you lose')
swg(comp_choice, player_choice)