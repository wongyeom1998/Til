# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    
    ans = ''
    while int(N) != N and len(ans) <= 13:
        A = (str(N*2)).split('.')
        if int(A[0]) == 1:
            ans =  ans + '1'
        else:
            ans =  ans +'0'
        N = float('0.' + A[1])
    if len(ans) == 14:
        ans = 'overflow'
    
    print(f'#{tc}', ans)