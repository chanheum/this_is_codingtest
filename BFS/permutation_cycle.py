n = []
list_n = []
ref_list = []
visited = []
result = 0
T = int(input())

def dfs(i, start):
    global result
    # 방문 했던 지점이면 체크안함
    if visited[i][start] == 1:
        return

    # 방문했던 지점이 아니면 방문 처리
    visited[i][start] = 1

    # 다음 방문할 곳이 이미 도착한 곳이라면 사이클 추가
    if visited[i][list_n[i][start]] == 1:
        result += 1
        return

    # 방문한 곳이랑 다음 방문할 곳이 같은 값이면 사이클 추가
    if start == list_n[i][start]:
        result += 1
        return

    # 아무 해당 사항 없다면 탐색
    dfs(i, list_n[i][start])

for num in range(T):
    n.append(int(input()))
    visited.append([0 for i in range(n[num] + 1)])
    ref_list.append([i for i in range(n[num] + 1)])
    list_n.append([0] + list(map(int, input().split(' '))))

for i in range(T):
    for num in range(1, n[i] + 1):
        dfs(i, num)
    print(result)
    result = 0