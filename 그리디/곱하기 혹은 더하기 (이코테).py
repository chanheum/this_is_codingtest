data = input()

result = int(data[0])

for i in len(1, len(data)):
    num = int(data[i])
    # 두 수 중에 하나라도 '0' 또는 '1'인 경우, 곱하기보단 더하기 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)