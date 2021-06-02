import sys
sys.setrecursionlimit(2000)
list_n = []
A, P = map(int,input().split(' '))

def calculate(number):
    result = 0
    str_n = str(number)

    for cha in str_n:
        num = int(cha)
        result += pow(num, P)

    return result

def dfs(start):
    ans = 0
    list_n.append(start)
    next = calculate(start)
    # print(list_n)

    for num in list_n:
        ans += 1
        if num == next:
            ans = ans - 1
            print(ans)
            return
    dfs(next)

dfs(A)