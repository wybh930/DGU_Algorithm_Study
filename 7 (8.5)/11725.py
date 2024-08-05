from collections import deque, defaultdict
import sys
input = sys.stdin.read

def find_parents(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    parents = [-1] * (n + 1)
    
    queue = deque([1])
    parents[1] = 0
    
    while queue:
        current = queue.popleft()
        for neighbor in tree[current]:
            if parents[neighbor] == -1:  
                parents[neighbor] = current
                queue.append(neighbor)
    
    result = []
    for i in range(2, n + 1):
        result.append(str(parents[i]))
    
    print("\n".join(result))

if __name__ == "__main__":
    data = input().strip().split()
    N = int(data[0])
    edges = []
    index = 1
    for _ in range(N - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    find_parents(N, edges)
