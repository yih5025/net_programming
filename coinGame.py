from random import randint

totalCoin = 50
count = 0

while(totalCoin > 0 and totalCoin < 100 ):
    coin = randint(1,2)
    guessCoin = int(input('코인을 맞추세요: '))

    if(guessCoin == coin):
        totalCoin += 9
        print('맞췄습니다. +9 점')
        count += 1
    else:
        totalCoin -= 10
        print('틀렸습니다. -10 점')
    
    print('현재 점수: ', totalCoin)

if(totalCoin >= 100):
    print('100점 입니다. 이겼습니다.')
elif(totalCoin <= 0):
    print('0점 입니다. 졌습니다.')
    
print('총 횟수: ', count)