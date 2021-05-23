# N = int(input())
# K = int(input())
# count = 0
#
# while(1):
#     if N % K != 0:
#         N -= 1
#         count += 1
#     else:
#         N //= K
#         count += 1
#
#     if N == 1:
#         break
#
# print(count)

# n, k = map(int, input().split())
#
# result = 0
#
# while True:
#     target = (n // k) * k # k로 나누어질 수 있는 가장 가까운 수 계산
#     result += (n - target)
#     n = target
#
#     # n이 k보다 작을 때 (더 이상 나눌 수 없을 때 반복문 탈출)
#     if n < k:
#         break
#     # k로 나누기.
#     result += 1
#     n //= k
#
# # 마지막으로 남은 수에 대하여 1씩 감산
# result += (n - 1)
# print(result)

# data = input()
# lst = list()
# result = 1
#
# for num in range(len(data)):
#     lst.append(int(data[num]))
#
# for n in range(len(lst)):
#     if lst[n] == 0 or lst[n] == 1:
#         result += lst[n]
#     else:
#         result *= lst[n]
#
# print(result)

# data = input()
#
# result = int(data[0])
#
# for i in len(1, len(data)):
#     num = int(data[i])
#     # 두 수 중에 하나라도 '0' 또는 '1'인 경우, 곱하기보단 더하기 수행
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)

# n = int(input())
# data = list(map(int, input().split()))
# data.sort() # 오름차순 정렬
#
# result = 0 # 총 그룹의 수
# count = 0  # 현재 그룹에 포함된 멤버의 수
#
# for i in data:
#     count += 1
#     if count >= i:  # 현재 포함된 멤버의 수가 현재 공포도보다 이상이면 그룹결성
#         result += 1 # 그룹 결성
#         count = 0   # 멤버의 수 초기화
#
# print(result)

# N = int(input())
# dir = list(map(str, input().split()))
#
# X, Y = 1, 1
#
# # 동, 북, 서, 남
# dx = { 'R':0, 'U':-1, 'L':0, 'D':1 }
# dy = { 'R':1, 'U':0, 'L':-1, 'D':0 }
#
# for data in dir:
#     X = X + dx[data]
#     Y = Y + dy[data]
#
#     if X > N or X < 1:
#         X -= dx[data]
#
#     if Y > N or Y < 1:
#         Y -= dy[data]
# print(X,Y)

# n = int(input())
# x,y = 1,1
# plans = input().split()
#
# # 서, 동, 북, 남
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types = ['L','R','U','D']
#
# # 이동 계획을 하나씩 확인하기
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#             print(nx, ny)
#     # 공간을 벗어나는 경우 다음 계획 확인
#     if nx < 1 or ny < 1 or nx > n or nx > n:
#         continue
#     # 범위를 벗어나지 않으면 이동 수행
#     x, y = nx, ny
#
# print(x,y)

# 완전 탐색 문제 (내 풀이)
# n = int(input())
# min, sec = 0, 0
# count = 0
# for hour in range(n+1):
#     for min in range(59+1):
#         for sec in range(59+1):
#             if str(hour).count('3') > 0 or str(min).count('3') > 0 or str(sec).count('3') > 0:
#                 count += 1
# print(count)

# 완전 탐색 문제 (나동빈 풀이)
# h = int(input())
# count = 0
#
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in (str(i)+str(j)+str(k)):
#                 count += 1
#
# print(count)

# # 왕실의 나이트 (내 풀이)
# n = input()
# x = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8 }
#
# # 나이트의 8가지 방향 벡터 정의
# dx = [1, -1, -1, 1, 2, 2, -2, -2]
# dy = [-2, -2, 2, 2, -1, 1, -1, 1]
#
# count = 0
#
# for num in range(8):
#     nx = x[n[0]] + dx[num]
#     ny = int(n[1]) + dy[num]
#     # 좌표계를 넘어가면 무시
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     count += 1
#
# print(count)

# # 왕실의 나이트 (나동빈 풀이)
# # 나이드의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,1),(1,2),(-1,2),(-2,1)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = column + step[0]
#     next_column = column + step[1]
#
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)

# 문자열 재정렬 (내 풀이)
input_data = list(map(str, input()))
input_data.sort()

result_num = 0
result_str = str()

for i in range(len(input_data)):
    if input_data[i] >= '1' and input_data[i] <= '9':
        result_num += int(input_data[i])
    else:
        result_str += input_data[i]

if result_num > 0:
    print(result_str + str(result_num))
else:
    print(result_str)

# 문자열 재정렬 (나동빈)
data = input()
result = []
value = 0

# 문자열을 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입!
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))