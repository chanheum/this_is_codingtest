n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k # k로 나누어질 수 있는 가장 가까운 수 계산
    result += (n - target)
    n = target

    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때 반복문 탈출)
    if n < k:
        break
    # k로 나누기.
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 감산
result += (n - 1)
print(result)