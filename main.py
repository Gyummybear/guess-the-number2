import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0  # 추가된 변수: 시도 횟수
    while guess != random_number and attempts < 3:  # 시도 횟수가 3 미만일 때만 반복
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        attempts += 1

    if guess == random_number:
        print(f'Yay, congrats! You guessed the number {random_number} correctly in {attempts} attempts.')
    else:
        print(f'Oops, you ran out of attempts! The number I was thinking of was {random_number}.')

guess(10)

