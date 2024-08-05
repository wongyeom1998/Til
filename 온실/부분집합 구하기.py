T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                continue
            result.append(arr[i][j] + arr[i+1][j] +arr[i][j-1] +arr[i-1][j]+arr[i][j+1])
    print(f'#{tc} {max(result)}')