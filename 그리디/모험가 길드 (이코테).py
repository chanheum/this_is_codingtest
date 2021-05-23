n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬

result = 0 # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 멤버의 수

for i in data:
    count += 1
    if count >= i:  # 현재 포함된 멤버의 수가 현재 공포도보다 이상이면 그룹결성
        result += 1 # 그룹 결성
        count = 0   # 멤버의 수 초기화

print(result)
