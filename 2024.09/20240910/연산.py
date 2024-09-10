from collections import deque
T = int(input())
for tc in range(1 ,T+1):
    N, M = map(int, input().split())
    q = deque([N])
    distance = [-1] * 2000000
    distance[N] = 0
    while q:
        node = q.popleft()
        for weight in [-1, 1, node, -10]:
            next = node+weight
            if 갈수 없으면 혹은 최단거리 아니면: continue 
            q.append(next)
            최단거리 업데이트

    1. 큐를 만든다.(시작 노드 넣기)
    2. visited 역할을 할 수 있는 애를 만든다.
        (최단거리의 경우 distance 같은 느낌으로 해결 가능)
    
        2-1. 시작 노드에 방문체크 
    
    3. 큐가 없을 때 까지 반복하라고 명령(while)
        1. 큐에서 원소 뽑기
        2. 갈 수 있는 방향 탐색(visited 등 사용)
        3. ... 필요내용 ...
        4. 큐에 갈 수 있는 방향의 원소 넣기
        5. 방문체크(or 최단거리 업데이트)