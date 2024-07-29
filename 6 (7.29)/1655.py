import heapq
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
max_heap = []
min_heap = []

output = []

index = 1

for _ in range(N):
    num = int(data[index])
    index += 1
    
    if len(max_heap) == 0 or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    # Rebalance heaps if necessary
    if len(max_heap) > len(min_heap) + 1:
        moved_value = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, moved_value)
    elif len(min_heap) > len(max_heap):
        moved_value = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -moved_value)
    
    # Determine the median
    output.append(-max_heap[0])

sys.stdout.write("\n".join(map(str, output)) + "\n")
