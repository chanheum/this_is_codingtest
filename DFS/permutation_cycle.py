import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

n = []
list_n = []
ref_list = []
visited = []
result = 0
T = int(input())
def dfs(start):
    visited[start] = 1
    # 다음 방문할 곳이 이미 도착한 곳이라면 사이클 추가
    if visited[list_n[start]] == 0:
        # 아무 해당 사항 없다면 탐색
        dfs(list_n[start])

for num in range(T):
    result = 0
    n = int(input())
    visited = [0 for i in range(n + 1)]
    ref_list = [i for i in range(n + 1)]
    list_n = [0] + list(map(int, input().split(' ')))
    for num in range(1, n + 1):
        if visited[num] == 0:
            dfs(num)
            result += 1
        print(result)
