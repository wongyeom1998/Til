def preorder(node):
    if node ==0:
        return
    
    print(node, end =' ' )
    preorder(left[node])
    preorder(right[node])
   
V = int(input())
arr = list(map(int,input().split()))
left = [0]* (V+1)
right = [0] * (V+1)

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] == child

