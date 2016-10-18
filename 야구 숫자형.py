import random

prob_rn = [0, 0, 0]

prob_rn[0] = random .randint(1, 9)  #Make first number

prob_rn[1] = random .randint(1, 9)  #Make second number
while prob_rn[0] == prob_rn[1]:
    prob_rn[1] = random.randint(1, 9)

prob_rn[2] = random .randint(1, 9)  #Make third number
while (prob_rn[0] == prob_rn[2]) or (prob_rn[1] == prob_rn[2]):
    prob_rn[2] = random.randint(1, 9)

prob = prob_rn[0] * 100 + prob_rn[1] * 10 + prob_rn[2]
print(prob)

count = 0       #count를 global 형태로 가져오기 위해 loop 밖에 위치(?)
info = []

while True:
    ans = None
    try:
        ans = int(input("Input number:"))
    except:
        continue

    if ans > 999 or ans < 0:
        continue

    count += 1      # count = count + 1
    strike = 0
    ball = 0

    for i in range(len(prob)):      #코드의 일반화 : 코드의 재활용 염두
        for j in range(len(ans)):
            if i == j and prob[i] == ans[j]:
                strike += 1
            if i != j and prob[i] == ans[j]:
                ball += 1

    info.append([strike, ball])

    if strike == 3:
        print("You did.")

        sum = [0, 0]
        for i in info:
            sum[0] += i[0]
            sum[1] += i[1]

        avg = [sum[0]/len(info), sum[1]/len(info)]

        print("Strike average : {} Ball average : {}" .format(avg[0], avg[1]))
        break

    print("Times : {} Strike : {} Ball : {}" .format(count, strike, ball))
