import heapq
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
heap = []

output = []
index = 1

for _ in range(N):
    x = int(data[index])
    index += 1
    
    if x == 0:
        if heap:
            output.append(-heapq.heappop(heap))
        else:
            output.append(0)
    else:
        heapq.heappush(heap, -x)

sys.stdout.write("\n".join(map(str, output)) + "\n")
