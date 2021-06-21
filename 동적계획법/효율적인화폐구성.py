# 정수 n,m을 입력받기
n,m = map(int,input().split())

# n개의 화폐단위 정보 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 생성
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행 (Bottom-Up)
d[0] = 0
# i : 탐색하고자 하는 횟수 (화폐 개수)
for i in range(n):
    # j : 확인하고자 하는 화폐 단위
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]]+ 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
