import sys
from itertools import permutations

input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = list(map(int, data[1:N+1]))
operators_count = list(map(int, data[N+1:]))

operators = ['+'] * operators_count[0] + ['-'] * operators_count[1] + ['*'] * operators_count[2] + ['/'] * operators_count[3]

unique_permutations = set(permutations(operators))

def calculate(expression):

    result = numbers[0]
    index = 1
    for op in expression:
        if op == '+':
            result += numbers[index]
        elif op == '-':
            result -= numbers[index]
        elif op == '*':
            result *= numbers[index]
        elif op == '/':
       
            if result < 0:
                result = -(-result // numbers[index])
            else:
                result //= numbers[index]
        index += 1
    return result

max_result = -float('inf')
min_result = float('inf')

for perm in unique_permutations:
    result = calculate(perm)
    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result

print(max_result)
print(min_result)
