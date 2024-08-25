import sys
input = sys.stdin.read

def min_plug_replacements(N, K, use_order):
    plugs = []
    replacements = 0
    
    for i in range(K):
        item = use_order[i]
        if item in plugs:
            continue
        
        if len(plugs) < N:
            plugs.append(item)
        else:
            furthest_use = -1
            plug_to_remove = None
            
            for plug in plugs:
                try:
                    next_use = use_order.index(plug, i + 1)
                except ValueError:
                    next_use = float('inf')
                
                if next_use > furthest_use:
                    furthest_use = next_use
                    plug_to_remove = plug
            
            plugs.remove(plug_to_remove)
            plugs.append(item)
            replacements += 1
    
    return replacements

data = input().split()
N = int(data[0])
K = int(data[1])
use_order = data[2:]

print(min_plug_replacements(N, K, use_order))
