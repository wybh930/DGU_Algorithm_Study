import itertools
import sys

def find_seven_dwarfs(heights):
    dwarfs = list(map(int, heights))

    for comb in itertools.combinations(dwarfs, 7):
        if sum(comb) == 100:
            return sorted(comb)  

input = sys.stdin.read().strip().split()

result = find_seven_dwarfs(input)
for height in result:
    print(height)
