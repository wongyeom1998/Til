def change(num):
    if num.isdecimal():
        A = ''
        while int(num) > 0:
            A = str(int(num) % 2) + A
            num = (int(num))//2
        return A
    else: 
        ten = int(num, base = 16)
        two = bin(ten)
        return two[2:]



T = int(input())
for tc in range(1, T+1):
    N, arr = input().split()
    changed = []
    for i in arr:
        changed.append(change(i))
    print(f'#{tc}', end = ' ')
    for i in changed:
        print(i, end = '')
    print()