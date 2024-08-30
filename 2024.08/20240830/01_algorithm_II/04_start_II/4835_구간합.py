T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    ai = list(map(int,input().split()))
    check =[]
    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += ai[i+j]
        check.append(temp)
    print(f'#{tc}', max(check)-min(check))