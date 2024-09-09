import sys

sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sp = []
    score = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                sp.append([i, j])  # 스타팅 포인트로 지정해 줄 만한 곳을 찾음
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 탐색할 수 있는 4방향
    wormhole = [6, 7, 8, 9, 10]  # 웜홀에 해당하는 숫자들

    for i in range(len(sp)):  # 스타팅 포인트를 하나씩 해서 출발 시켜줌
        for k, p in dxy:  # 방향별로
            arr[sp[i][0]][sp[i][1]] = 99  # 출발 지점을 99로 지정해 줌. *다만 다음번 돌 때 arr를 초기화 해주는 방법을 모르겠음
            tempscore = 0  # 돌 때마다의 점수를 score에 기록해서 최고 점수를 뽑아내기 위한 변수
            nx = sp[i][0] + k  # 출발
            ny = sp[i][1] + p
            print(nx, ny , score)
            if 0 <= nx < N and 0 <= ny < N:  # arr의 범위를 넘지 않는 한에서
                while arr[nx][ny] != 99 and arr[nx][ny] != -1 and 0 <= nx < N and 0 <= ny < N:  # 제자리로 돌아올 때나 블랙 홀을 만나면 멈춤
                    if arr[nx][ny] == 0:  # 만약 아무것도 없는 빈 공간이면
                        nx = nx + k
                        ny = ny + p  # 그 방향 그대로 전진
                        continue
                    if arr[nx][ny] == -1 or arr[nx][ny] == 99:  # 만약 블랙홀이나 제자리로 돌아오면
                        score.append(tempscore)  # 그때까지의 점수를 더하고 while문 스탑
                        break
                    elif arr[nx][ny] in wormhole:  # 웜홀을 만나게 되면
                        for r in range(len(arr)):
                            for c in range(len(arr[r])):
                                if arr[r][c] == arr[nx][ny] and r != nx and c != ny:  # 같은 값이지만 다른 위치인 곳 , 즉 다른 웜홀을 찾아서
                                    a = r + k  # 그방향 그대로 진행
                                    b = c + p    
                        nx = a
                        ny = b
                        continue

                    elif nx == 0 and k == -1 and p == 0 and arr[nx][ny] == 0:  # 위쪽 벽과 부딪힐 때
                        k = 1
                        p = 0
                        nx = nx + k
                        ny = ny + p
                        tempscore += 1
                        continue
                    elif ny == 0 and k == 0 and p == -1  and arr[nx][ny] == 0:  # 왼쪽 벽과 부딪힐 때
                        k = 0
                        p = 1
                        nx = nx + k
                        ny = ny + p
                        tempscore += 1
                        continue
                    elif nx == N - 1 and k == 1 and p == 0  and arr[nx][ny] == 0:  # 아래쪽 벽과 부딪힐 때
                        k = -1
                        p = 0
                        nx = nx + k
                        ny = ny + p
                        tempscore += 1
                        continue
                    elif ny == N - 1 and k == 0 and p == 1  and arr[nx][ny] == 0:  # 오른쪽 벽과 부딪힐 때
                        k = 0
                        p = -1
                        nx = nx + k
                        ny = ny + p
                        tempscore += 1
                        continue

                    elif arr[nx][ny] == 1:  # 1과 부딪힐 때
                        if k == 0 and p == 1:  # 오른쪽으로 가다가 부딪힐때

                            tempscore += 1
                            k = 0
                            p = -1
                            nx = nx + k
                            ny = ny + p
                            continue

                        elif k == 1 and p == 0:  # 아래쪽으로 가다가 부딪힐때
                            tempscore += 1
                            k = 0
                            p = 1
                            nx = nx + k
                            ny = ny + p
                            continue

                        elif k == 0 and p == -1:  # 왼쪽으로 가다가 부딪힐때
                            k = -1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == -1 and p == 0:  # 위쪽으로 가다가 부딪힐때
                            k = 1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue


                    elif arr[nx][ny] == 2:  # 2 블럭과 부딪힐 때
                        if k == 0 and p == 1:
                            k = 0
                            p = -1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == 1 and p == 0:
                            k = -1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == 0 and p == -1:
                            k = 1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == -1 and p == 0:
                            k = 0
                            p = 1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue


                    elif arr[nx][ny] == 3:  # 3블럭과 부딪힐 때
                        if k == 0 and p == 1:
                            k = 1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == 1 and p == 0:
                            k = -1
                            p = 1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == 0 and p == -1:
                            k = 0
                            p = 1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == -1 and p == 0:
                            k = 0
                            p = -1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue


                    elif arr[nx][ny] == 4:  # 4블럭과 부딪힐 때
                        if k == 0 and p == 1:
                            k = -1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1

                            continue

                        elif k == 1 and p == 0:
                            k = 0
                            p = -1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == 0 and p == -1:
                            k = 0
                            p = 1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                        elif k == -1 and p == 0:
                            k = 1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue

                    elif arr[nx][ny] == 5:  # 5 블럭과 부딪힐 때
                        if k == 0 and p == 1:
                            k = 0
                            p = -1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue
                        elif k == 1 and p == 0:
                            k = -1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue
                        elif k == 0 and p == -1:
                            k = 0
                            p = 1
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue
                        elif k == -1 and p == 0:
                            k = 1
                            p = 0
                            nx = nx + k
                            ny = ny + p
                            tempscore += 1
                            continue
    print(max(score))