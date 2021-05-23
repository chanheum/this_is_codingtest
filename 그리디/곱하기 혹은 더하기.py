data = input()
lst = list()
result = 1

for num in range(len(data)):
    lst.append(int(data[num]))

for n in range(len(lst)):
    if lst[n] == 0 or lst[n] == 1:
        result += lst[n]
    else:
        result *= lst[n]

print(result)