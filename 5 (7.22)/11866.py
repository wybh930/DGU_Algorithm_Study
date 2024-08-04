from collections import deque

def josephus_permutation(N, K):
 
    people = deque(range(1, N + 1))
    result = []
    
    while people:
      
        people.rotate(-(K - 1))
      
        result.append(people.popleft())
    
    print("<" + ", ".join(map(str, result)) + ">")

N, K = map(int, input().split())

josephus_permutation(N, K)

