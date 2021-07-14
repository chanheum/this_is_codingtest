from collections import deque
v, e = map(int, input().split())

# 진입 차수
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동 가능
    # 진입 차수 1 증가
    indegree[b] += 1

def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때가지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입 차수에서 1빼기
        for i in graph[now]:
            indegree[i] -=1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = ' ')

topology_sort()