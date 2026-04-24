import random

def generate():
    return random.randint(1, 6)

def main():
    while True:
        input('Press Enter to roll the dice...')
        result = generate()
        print(f'You rolled a {result}!')
        play_again = input('Do you want to roll again? (yes/no): ').lower()
        if play_again == 'no':
            print('Thanks for playing!')
            break

main()