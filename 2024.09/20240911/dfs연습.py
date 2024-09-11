import sys
sys.stdin = open('graph.txt')

def dfs(node):
    print(node, end = ' ')
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        else:
            visited[next_node] = 1
            dfs(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
visited[1]=1
dfs(1)