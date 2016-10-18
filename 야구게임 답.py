import random
#ramdom한 수를 발생시키는 함수#

prob_rn = [0, 0, 0]

prob_rn[0] = random .randint(1, 9)  #Make first number

prob_rn[1] = random .randint(1, 9)  #Make second number
while prob_rn[0] == prob_rn[1]:
    prob_rn[1] = random.randint(1, 9)

prob_rn[2] = random .randint(1, 9)  #Make third number
while (prob_rn[0] == prob_rn[2]) or (prob_rn[1] == prob_rn[2]):
    prob_rn[2] = random.randint(1, 9)

prob = str(prob_rn[0]) + str(prob_rn[1]) + str(prob_rn[2])
print(prob)

count = 0       #count를 global 형태로 가져오기 위해 loop 밖에 위치(?)

#ALLSTRIKE = 0      #방법1
#ALLBALL = 0

#ALLSTRIKE = []     방법2
#ALLBALL = []

info = []

while True:
    ans = input("Input number:")        #string 형태로 입력

#    ct = 0

    if not ans.isdigit():       #숫자형이 아니면 재입력
        print("Please input only number.")
        continue

    if len(ans) != 3:       #space나 숫자를 3개 이상 입력 시 재입력
        print("Please input number together.")
        continue

#for i in range(len(ans)):       #(내가 짠)중복숫자 방지
 #       for j in range(len(ans)):
  #          if i != j and ans[i] == ans[j]:
 #             ct += 1

    #if ct > 0:
     #   print("Please input different number for each section.")
      #  continue

    t = list(set(ans)) #set은 중복 허용하지 않고 unique만 list에 포함

    if len(t) != 3:     #중복숫자 방지
        print("Do not duplicate.")
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

#    ALLSTRIKE += strike        #방법1
#    ALLBALL += ball

    #ALLSTRIKE.append(strike)       방법2
    #ALLBALL.appent(ball)

    info.append([strike, ball])

    if strike == 3:
        print("You did.")

        sum = [0, 0]
        for i in info:
            sum[0] += i[0]
            sum[1] += i[1]

        avg = [sum[0]/len(info), sum[1]/len(info)]

        #sum = 0            방법2
        #for i in ALLSTRIKE:
        #    sum += i
        #strike_avg = sum / count

        #sum = 0
        #for j in ALLBALL:
        #    sum += j
        #ball_avg = sum / count     방법2 끝

        #print("Strike average : {} Ball average : {}" .format(strike_avg, ball_avg))       방법2
        #print("Mean strike : {} Mean ball : {}".format(ALLSTRIKE / count, ALLBALL / count))    #방법1
        print("Strike average : {} Ball average : {}" .format(avg[0], avg[1]))
        break

    print("Times : {} Strike : {} Ball : {}" .format(count, strike, ball))

