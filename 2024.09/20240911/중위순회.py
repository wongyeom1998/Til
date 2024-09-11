import sys
sys.stdin = open('input3.txt')

def mid(tree):
    pass





T =10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].isdigit():
                arr[i][j] = int(arr[i][j])
    tree = [0] * (N+1)
    for i in arr:
        tree[i[0]] = i[1]
    