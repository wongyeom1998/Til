selected = [0] * 3 # 1,3,7으로 이루어진 집합의 부분집합 구하기
num_list = [1,3,7]
for i in range(2):
    selected[0] = i
    for j in range(2):
        selected[1] = j
        for k in range(2):
            selected[2] = k
            subset = []
            for p in range(3):
                if selected[p] == 1:
                    subset.append(num_list[p])
            print(subset)