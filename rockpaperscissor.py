import random

user_Wins = 0
computer_Wins = 0
options = ['rock', 'scissors', 'paper']
print('Hello user, and welcome to Rock Paper Scissors! You will be presented with three options (rock, paper, or scissors) and will have to face a computer, competing against you.')

while True:
    user_input = input('Type rock, paper, scissors - or to quit type Q: ').lower()

    if user_input == 'q':
        break
    
    if user_input not in options:
        continue
    
    computer_input = options[random.randint(0,2)]
    
    if user_input == 'rock' and computer_input == 'scissors':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you win!')
        user_Wins += 1
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'rock' and computer_input == 'paper':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you lose!')
        computer_Wins += 1
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')
        
    if user_input == 'rock' and computer_input == 'rock':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you drew!')
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'paper' and computer_input == 'scissors':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you lose!')
        computer_Wins += 1
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'paper' and computer_input == 'rock':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you win!')
        user_Wins += 1
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'paper' and computer_input == 'paper':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you drew!')
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'scissors' and computer_input == 'scissors':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you drew!')
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'scissors' and computer_input == 'rock':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you lose!')
        computer_Wins += 1
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')

    if user_input == 'scissors' and computer_input == 'paper':
        print(f'You picked {user_input}, and the computer picked {computer_input}, you win!')
        user_Wins += 1
        print(f'Your wins: {user_Wins}\nComputer wins: {computer_Wins}')
        
print('Thanks for playing!')




