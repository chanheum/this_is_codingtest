N = int(input())
dir = list(map(str, input().split()))

X, Y = 1, 1

# 동, 북, 서, 남
dx = { 'R':0, 'U':-1, 'L':0, 'D':1 }
dy = { 'R':1, 'U':0, 'L':-1, 'D':0 }

for data in dir:
    X = X + dx[data]
    Y = Y + dy[data]

    if X > N or X < 1:
        X -= dx[data]

    if Y > N or Y < 1:
        Y -= dy[data]
print(X,Y)
