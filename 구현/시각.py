n = int(input())
min, sec = 0, 0
count = 0
for hour in range(n+1):
    for min in range(59+1):
        for sec in range(59+1):
            if str(hour).count('3') > 0 or str(min).count('3') > 0 or str(sec).count('3') > 0:
                count += 1
print(count)