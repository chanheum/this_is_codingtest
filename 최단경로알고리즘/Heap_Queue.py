import heapq
# heapq 자료구조는 Default로 오름차순에 맞게 적용되어있어서
# 내림차순을 구현하려면 heapq 자료구조로 데이터를 리스트에 넣을 때 -연산만 해주면 된다.

# 오름차순 힙 정렬 (Heap Sort)
def heapsort_up(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort_up([1,3,5,7,9,2,4,6,8,0])
print(result)

# 내림차순 정렬
def heapsort_down(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort_down([1,3,5,7,9,2,4,6,8,0])
print(result)

