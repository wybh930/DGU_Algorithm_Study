import sys

def calculate_total_length(trees, height):
    total_length = 0
    for tree in trees:
        if tree > height:
            total_length += tree - height
    return total_length

def find_max_height(trees, M):
    left, right = 0, max(trees)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        total_length = calculate_total_length(trees, mid)
        
        if total_length >= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
trees = list(map(int, data[2:N+2]))

result = find_max_height(trees, M)
print(result)
