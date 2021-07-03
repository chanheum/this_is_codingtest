# 노드의 개수가 1000개 이상부터는 연산개수가 1000억이 되므로 노드 개수가 적을 때 써야함.
# 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N^3).
INF = int(1e9)
# 노드의 개수 입력
n = int(input())
# 간선의 개수 입력
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 '0'으로 초기화.
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 각 간선 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    # a노드에서 b노드로 가는데 드는 비용이 'c'임으로 설정
    graph[a][b] = c

# 점화식에 따라 플로이트 워셜 알고리즘 수행 (3중 for문)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY",end="")
        else:
            print(graph[a][b], end="")
    print()