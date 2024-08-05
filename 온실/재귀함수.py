def sum_of_digits(number):
    '''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
    if number < 10 :
        return number
    else:   
        return number%10 + sum_of_digits(number // 10)
result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6
