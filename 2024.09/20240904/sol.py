import sys
sys.stdin = open('input.txt')

def finding(l,r,A,k):
    
    check = []
    while l <= r:
        m = (l+r)//2
        if A[m] == k:
            check.append('good')
            break
        elif A[m] > k:
            if len(check) >= 1 and check[-1] == 'right':
                break
            check.append('right')
            r = m-1
        else:
            if len(check) >= 1 and check[-1] == 'left':
                break
            check.append('left')
            l = m+1
    return check

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    l = 0
    r = N -1
    check = []
    for k in B:
        check.append(finding(l,r,A,k))
    result = 0
    
    for i in check:
        if 'good' in i:
            result +=1
    print(f'#{tc}', result)
        