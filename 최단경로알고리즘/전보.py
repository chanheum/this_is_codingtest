import heapq
INF = int(1e9)
# 도시의 개수, 통로의 개수, 보내고자하는 도시
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
spent_time = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input())
    # 도시 a에서 b로 가는데 걸리는 시간이 'c'라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)
        if spent_time[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < spent_time[i[0]]:
                spent_time[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

count = 0
max_time = 0
for d in spent_time:
    if d != 1e9:
        count += 1
        max_time = max(max_time, d)

print(count-1, max_time)