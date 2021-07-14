# 특성 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출 (부모의 루트 노드 탐색)
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은값이 부모루트가 되도록 지정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선 (Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화 하기

# 부모 테이블 상태에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

Cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent, b):
        Cycle = True
        break
    else:
        union_parent(parent,a,b)

if Cycle:
    print('사이클이 발생했습니다')
else:
    print('사이클이 발생하지 않았습니다.')