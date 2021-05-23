n = input()
x = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8 }

# 나이트의 8가지 방향 벡터 정의
dx = [1, -1, -1, 1, 2, 2, -2, -2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

count = 0

for num in range(8):
    nx = x[n[0]] + dx[num]
    ny = int(n[1]) + dy[num]
    # 좌표계를 넘어가면 무시
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)