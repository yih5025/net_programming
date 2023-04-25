from random import randint
count = 0;
random_number = randint(1, 100)

guess = input("1 부터 100 까지 숫자를 맞춰보세요.")

while guess != random_number and count <= 4:
    guess = eval(input('Enter your guess(1-100): '))
    count = count + 1
    if guess < random_number:
        print('더 큽니다.', 5-count, '회 남았습니다.\n')
    elif guess > random_number:
        print('더 작습니다.', 5-count, '회 남았습니다.\n')
    else:
        print('맞습니다!')

if count == 5 and guess != random_number:
    print('당신이 졌습니다. 정답은 ', random_number, '입니다.')

