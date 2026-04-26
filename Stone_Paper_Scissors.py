import random

score_player = 0
score_computer = 0

def generate():
    l = ['Stone', 'Paper', 'Scissors']
    return random.choice(l)

def check_win(player, computer):
    global score_player, score_computer
    if player == computer:
        return 'It is a tie'
    elif player == 'Stone':
        if computer == 'Scissors':
            score_player += 1
            return '**********   Hurreyyyy!!!!!!! YOU WIN   **********'
        else:
            score_computer += 1
            return 'Better luck next time'
    elif player == 'Paper':
        if computer == 'Stone':
            score_player += 1
            return '**********   Hurreyyyy!!!!!!! YOU WIN   **********'
        else:
            score_computer += 1
            return 'Better luck next time'
    elif player == 'Scissors':
        if computer == 'Paper':
            score_player += 1
            return '**********   Hurreyyyy!!!!!!! YOU WIN   **********'
        else:
            score_computer += 1
            return 'Better luck next time'

def main():
    l = ['Stone', 'Paper', 'Scissors']
    while True:
        n = input("Press 1 to play and 2 to exit: ")
        if n.isdigit():
            n = int(n)
            if n == 1:
                player = input('Enter your choice (Stone, Paper, Scissors): ').capitalize()
                if player not in l:
                    print('Invalid choice. Please try again.')
                    continue
                computer = generate()
                print(f'Computer chose: {computer}')
                result = check_win(player, computer)
                print(result)
            elif n == 2:
                print('Thanks for playing!, Hope you had fun playing the game.')
                print('Your score: ', score_player)
                print('Computer score: ', score_computer)
                print('See you soon!!!!')
                break
            else:
                print('Invalid choice.')
        
        else:
            print('Invalid input. Please enter a number.')

print('Welcome to the Stone, Paper, Scissors Game!')
main()
