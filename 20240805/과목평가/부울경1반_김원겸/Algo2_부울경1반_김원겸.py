T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    K = [-1]

    for i in range(N-1):
        if A[i+1] < A[i]:
            K.append(i)
    K.append(N)
    S = []
    for j in range(len(K)-1):
        S.append(A[K[j]+1:K[j+1]+1])
    P = [] # 경사
    V = [] # 그 길이
    for i in S:
        F = i[-1] -i[0]
        G =len(i)
        V.append(G)
        if F/G == 0:
            continue
        else:
            P.append(F / G)
    D = list(zip(P,V))
    for i in range(len(D)-1):
        if D[i][0] <= D[i+1][0]:
            D[i],D[i+1] =D[i+1],D[i]
    for i in range(len(D)-1):
        if D[i][0] == D[i+1][0] and D[i][1] > D[i+1][1]:
            D[i],D[i+1] =D[i+1],D[i] 
    print(D[-1][1])
    
    