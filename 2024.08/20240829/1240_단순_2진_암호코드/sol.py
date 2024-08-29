# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # M은 가로크기, N은 세로크기 
    arr = [list(input()) for _ in range(N)]
    print(arr)
    check_arr = []
    for i in arr:
        for j in range(M):
            if i[M-j] == 1:
                for k in range(56):
                    check_arr.append(arr[i][M-j+k])
            break
    