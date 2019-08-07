# baseball game
import random
answer = list(random.sample(range(1, 10), 3))  #임의의 숫자 3개를 호출

print(answer)

print ('★☆★☆★☆★☆숫자야구게임★☆★☆★☆★☆\n{0:-^50}\n규칙 ▶ 숫자는 1~9까지 겹치지 않게 3개 입력한다'.format(''))
try_ = 0
strike = 0
ball = 0

while strike < 3:
    num = input('숫자를 입력하세요')
    # 중복 숫자를 거르기 위한 수식
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

    strike = 0
    ball = 0

#베이스볼 규칙
    for i in range(0,3):
        for j in range(0,3):
            if (num[i] == str(answer[j]) and i==j):
                strike += 1
            elif (num[i] == str(answer[j]) and i!=j):
                ball += 1
    try_ += 1
    print(try_,'회 결과 : ',strike, '스트라이크',ball,'볼','\n')

print ('{0:-^50}'.format(''))
print ('게임에서 승리하셨습니다')
