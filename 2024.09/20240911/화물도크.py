import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    K = [list(map(int, input().split())) for _ in range(N)]

    hour = [0] * 25
    for i in range(N):
        for i in range(len(K)-1):
            if K[i][1] >= K[i+1][1]:
                K[i], K[i+1] = K[i+1], K[i]
    count = 0
    for i in K:
        cnt =0
        for j in range(i[0],i[1]+1):
            if hour[j] == 0:
                cnt +=1

        if cnt == i[1]+1 - i[0]:
            for j in range(i[0],i[1]):
                hour[j] = 1
            count+=1
    print(count)