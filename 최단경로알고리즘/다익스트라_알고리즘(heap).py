import heapq
import sys

Input = sys.stdin.readline()
INF = int(1e9)
# n : 노드의 개수, m : 간선의 개수
n , m = map(int,input().split())
start = int(input())
# 노드에 대한 연결정보를 저장할 데이터
graph = [[] for _ in range(n + 1)]
# 현재 노드에 대한 최소 비용을 저장할 데이터
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미로 저장
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드에 대해서는 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            # 현재 노드에 연결된 다른 인접한 노드들로 향하기 위한 비용
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])