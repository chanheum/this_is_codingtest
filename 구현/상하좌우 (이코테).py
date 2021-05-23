n = int(input())
x,y = 1,1
plans = input().split()

# 서, 동, 북, 남
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx, ny)
    # 공간을 벗어나는 경우 다음 계획 확인
    if nx < 1 or ny < 1 or nx > n or nx > n:
        continue
    # 범위를 벗어나지 않으면 이동 수행
    x, y = nx, ny

print(x,y)