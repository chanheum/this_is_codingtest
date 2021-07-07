INF = int(1e9)
N, M = map(int,input().split())
# 무한을 의미하는 값으로 10억을 설정
graph = [[INF] * (N+1) for _ in range(N + 1)]

# 자기 자신에서 자기 자신으로 가는 경우는 0으로 초기화
for a in range(N+1):
    for b in range(N+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력 받아서, 그 값으로 양방향 초기화
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 k와 최종 목적지 노드 x를 입력 받기
k, x = map(int, input().split())

for k in range(N+1):
    for i in range(N + 1):
        for j in range(N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)