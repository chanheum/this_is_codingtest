n, m = map(int,input().split(' '))
graph = list()
result = 0

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 탈출 정보부터 수행 (주어진 범위를 벗어나는 경우에는 즉시 종료)
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 해당 노드 방문처리
        dfs(x-1, y) # 상
        dfs(x,y-1)  # 하
        dfs(x+1,y)  # 좌
        dfs(x,y+1)  # 우 탐색
        return True
    else:
        pass

    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            # 방문했다면 증가
            result += 1

print(result)