import heapq
import sys
def dijkstra(N, graph, start, end):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return dist[end]

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        cost = int(data[index + 2])
        index += 3
        graph[u].append((v, cost))
    
    start = int(data[index])
    end = int(data[index + 1])
    
    result = dijkstra(N, graph, start, end)
    print(result)

if __name__ == "__main__":
    main()
