# ------------내 풀이 (오답) -----------------------------
# from collections import deque
# n, m = map(int, input().split())
# # miro = [[0] * (m) for i in range(n)]
# miro = []
# visited = [[0] * (m) for i in range(n)]
# # print(miro)
# # print(visited)
# # 동 북 서 남
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
#
# for i in range(n):
#     miro.append(list(map(int, input())))
#
# print(miro)
#
# def bfs(x,y):
#     result = 0
#     visited[x][y] = 1
#     result += 1
#     queue = deque([miro[x][y]])
#
#     while queue:
#         queue.popleft()
#         result += 1
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 print(nx, ny, '= fail')
#                 continue
#
#             if visited[nx][ny] == 0 and miro[nx][ny] == 1:
#                 print(nx, ny, '= success')
#                 visited[nx][ny] = 1
#                 queue.append([miro[nx][ny]])
#                 x = nx
#                 y = ny
#     return result
# print(bfs(0,0))
# -------------이코테 + 내 풀이------------------------------------------
from collections import deque
n, m = map(int, input().split())
# miro = [[0] * (m) for i in range(n)]
miro = []
visited = [[0] * (m) for i in range(n)]
# print(miro)
# print(visited)
# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    miro.append(list(map(int, input())))

# print(miro)

def bfs(x,y):
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재방향에서 4가지 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if miro[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if visited[nx][ny] == 0 and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 하단 최단 거리 반환
    return miro[n-1][m-1]
print(bfs(0,0))