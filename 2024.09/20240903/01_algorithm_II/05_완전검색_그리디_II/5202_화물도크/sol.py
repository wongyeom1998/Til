def check(lev):
    if lev == 10:
        return
    for i in range()




import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1 ,T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    start_point = sorted(time)
    result_list = []
    for i in start_point:
        result = 0
        for j in range(2):
            if j == 0:
                continue
            if j == 1:
                result +=1
                for k in time:
                    if i[1] <= k[0]:
                        result +=1