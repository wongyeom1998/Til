
def preorder(node):
    
    if node == 0:
        return
    temp.append(node)
    preorder(left[node])
    preorder(right[node])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int,input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    temp =[]
    for i in range(0 , len(arr), 2):
        parent, child = arr[i], arr[i+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    preorder(N)
    print(len(temp))