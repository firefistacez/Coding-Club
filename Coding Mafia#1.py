limit = int(input("Input:"))
input_numbers = input("")
userList = input_numbers.split()
number = 1
last = len(userList)
answerList = []
for i in range(last-1):
    answer = 0
    if i<5:
        for j in range(i+1):
            answer = answer + int(userList[j])
        answer = answer/number
        answerList.append(round(answer,4))
        if number < 5:
            number += 1
    else: 
        for j in range(i-4,i+1):
            answer = answer + int(userList[j])
        answer = answer/number
        answerList.append(round(answer,4))

for i in range(last-1):
    print(answerList[i],end =" ")
