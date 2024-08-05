T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    Aij = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            temp = Aij[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                    temp = temp + Aij[ni][nj]
            result.append(temp)
    for y in range(len(result)-1):
        if result[y] >= result[y+1]:
            result[y],result[y+1] = result[y+1],result[y]
    print(result[-1])