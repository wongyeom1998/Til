def change(num):
    B = int(num, base =16)
    C = bin(B)
    changed.append(C)


T = int(input())
for tc in range(1, T+1):
    N, arr = input().split()
    changed =[]
    for i in arr:
        change(i)
    print(f'#{tc}',end=' ')
    for i in changed:
        print(i[2:].zfill(4), end='')
        print('\n')
    