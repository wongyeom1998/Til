# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)


# 사용 후
squared_numbers2 = [num**2 for num in numbers]
squared_numbers2 = list(num**2 for num in numbers)
print(squared_numbers2)

# List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * (5) for _ in range(5)]
print(data1)
# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]

#변수 쓸일이 없으면 _ 반복의 횟수가 중요하고 변수가 안중요하면 언더바
print(data2)

# 리스트 생성을 하는 경우에만 컴프리헨션을 쓰자


