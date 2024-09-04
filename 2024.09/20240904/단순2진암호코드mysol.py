import sys
sys.stdin = open('input.txt')

def finding(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][M-j-1] == '1':
                password = arr[i][M-j-56:M-j]
                return password


T =int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N 세로 크기, M 가로크기
    arr = [list(input()) for _ in range(N)]
    password = finding(arr)
    divide = []
    for i in range(0, len(password), 7):
        temp = password[i:i+7]
        divide.append(tuple(temp))
    dictionary = {('0','0','0','1','1','0','1') : 0,
                  ('0','0','1','1','0','0','1') : 1,
                  ('0','0','1','0','0','1','1') : 2,
                  ('0','1','1','1','1','0','1') : 3,
                  ('0','1','0','0','0','1','1') : 4,
                  ('0','1','1','0','0','0','1') : 5,
                  ('0','1','0','1','1','1','1') : 6,
                  ('0','1','1','1','0','1','1') : 7,
                  ('0','1','1','0','1','1','1') : 8,
                  ('0','0','0','1','0','1','1') : 9
                  }
    result =[]
    for i in divide:
        result.append(dictionary[i])
    odd = 0
    part = 0
    for i in range(0,len(result),2):
        odd += result[i]
        part += result[i+1]
    if (odd *3 + part) % 10 == 0:
        hap = 0
        for i in result:
            hap += i
        print(f'#{tc}', hap)
    else: print(f'#{tc}', 0)