def solution(progresses, speeds):
    needday =[]
    for i in range(len(progresses)):
        num = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            num +=1
        needday.append(num)
    needday.append(101)
    current = 0
    result = []
    for i in range(len(needday)):
        if needday[current] < needday[i]:
            result.append(i-current)
            current = i                                                  
    return result 
print(solution([93, 30, 55], [1, 30, 5]))

def solution(progresses, speeds):
    needday =[]    
    for i in range(len(progresses)):
        day = (100 - progresses[i])//speeds[i] 
        if (100 - progresses[i]) % speeds[i] != 0:
            day +=1
            needday.append(day)
        else :                  
            needday.append(day)
    needday.append(101)
    current = 0
    result = []
    for i in range(len(needday)):
        if needday[current] < needday[i]:
            result.append(i-current)
            current = i                                                  
    return result
print(solution([93, 30, 55], [1, 30, 5]))