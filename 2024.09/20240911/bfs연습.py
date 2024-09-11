import sys
sys.stdin = open('graph.txt')

def bfs(node):
    q = [node]
    while q:
        now = q.pop(0)
        print(now, end = ' ')
        for next_node in graph[now]:
            if visited[next_node] == 1:
                continue
            else:
                visited[next_node] = 1
                q.append(next_node)



N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1]= 1
bfs(1)