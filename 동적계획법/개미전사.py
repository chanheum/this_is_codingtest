# 정수 n을 입력받기
n = int(input())
# 식량 정보 입력받기
array = list(map(int, input().split()))
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(100)]

# 다이나믹 프로그래밍 진행 (Bottom-Up 방식)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    # i-1까지 계산한 최적의 해
    # i-2까지 계산한 최적의 해 + i번째 식량을 더했을 때 최적의 해 비교
    d[i] = max(d[i-1], d[i-2]+array[i])

# 계산된 결과 출력
print(d[n-1])