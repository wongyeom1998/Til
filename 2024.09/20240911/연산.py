from collections import deque

def bfs():
    while q:
        node = q.popleft()
        for weight in [-1, 1, node, -10]:
            next = node+weight
            if 0 < next <= 1000000 and distance[next] == -1:
                if next != M:
                    distance[next] = distance[node] +1
                    q.append(next)
                if next == M:
                    return distance[node]+1
                    

T = int(input())
for tc in range(1 ,T+1):
    N, M = map(int, input().split())
    q = deque([N])
    distance = [-1] * 2000000
    distance[N] = 0
    print(bfs())

    
 