import random

def generate():
    l = ['Stone', 'Paper', 'Scissors']
    return random.choice(l)

def check_win(player, computer):
    if player == computer:
        return 'It is a tie'
    elif player == 'Stone':
        if computer == 'Scissors':
            return '**********   Hurreyyyy!!!!!!! YOU WIN   **********'
        else:
            return 'Better luck next time'
    elif player == 'Paper':
        if computer == 'Stone':
            return '**********   Hurreyyyy!!!!!!! YOU WIN   **********'
        else:
            return 'Better luck next time'
    elif player == 'Scissors':
        if computer == 'Paper':
            return '**********   Hurreyyyy!!!!!!! YOU WIN   **********'
        else:
            return 'Better luck next time'

def main():
    l = ['Stone', 'Paper', 'Scissors']
    while True:
        player = input('Enter your choice (Stone, Paper, Scissors): ').capitalize()
        if player not in l:
            print('Invalid choice. Please try again.')
            continue
        computer = generate()
        print(f'Computer chose: {computer}')
        result = check_win(player, computer)
        print(result)

print('Welcome to the Stone, Paper, Scissors Game!')
main()
