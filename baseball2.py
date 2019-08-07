# baseball game
git init

import random
random_num = random.sample(range(1, 10), 3)  #임의의 숫자 3개를 호출
print(random_num)

try_ = 0
strike = 0
ball = 0

print ('★☆★☆★☆★☆숫자야구게임★☆★☆★☆★☆\n{0:-^50}\n규칙 ▶ 숫자는 1~9까지 겹치지 않게 3개 입력한다'.format(''))

#중복 숫자를 거르기 위한 수식
while strike < 3:
    num = input('숫자를 입력하세요')

    if num[0] == num[1] == num[2]:
        print ('서로 다른 다시 숫자를 입력해주세요')
        continue
    elif num[0] == num[1]:
        print('서로 다른 다시 숫자를 입력해주세요')
        continue
    elif num[0] == num[2]:
        print('서로 다른 다시 숫자를 입력해주세요')
        continue
    elif num[1] == num[2]:
        print('서로 다른 다시 숫자를 입력해주세요')
        continue
    else:
        pass

#베이스볼 규칙
while strike < 3
for i in range(0,3):
    try_ += 1
    for j in range(0,3):
        if num[i] == num[j]:
            strike += 1

        elif num[i] != num[j]:
            ball += 1

    if strike == 3:
        print (str(strike),'스트라이크, 아웃!',str(try_),'만에 승리하셨습니다')
        break
    else:
        print (str(try_),'회 게임 결과',str(strike),'스트라이크',str(ball)'볼')
        print (try_+1,'게임을 다시 시작하세요')
        strike = 0
        ball = 0
        continue




