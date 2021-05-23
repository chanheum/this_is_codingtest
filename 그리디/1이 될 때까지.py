N = int(input())
K = int(input())
count = 0

while(1):
    if N % K != 0:
        N -= 1
        count += 1
    else:
        N //= K
        count += 1

    if N == 1:
        break

print(count)

