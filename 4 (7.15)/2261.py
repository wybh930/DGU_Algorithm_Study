import sys
import math

input = sys.stdin.read

def closest_pair_of_points(points):
    # Sort points by x-coordinate
    points.sort(key=lambda p: p[0])

    def distance_squared(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def closest_pair(low, high):
        if low == high:
            return float('inf')
        mid = (low + high) // 2
        mid_x = points[mid][0]
        d1 = closest_pair(low, mid)
        d2 = closest_pair(mid + 1, high)
        min_d = min(d1, d2)
        
        # Merge step
        temp = []
        for i in range(low, high + 1):
            if (points[i][0] - mid_x) ** 2 <= min_d:
                temp.append(points[i])
        
        temp.sort(key=lambda p: p[1])
        
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                if (temp[j][1] - temp[i][1]) ** 2 >= min_d:
                    break
                min_d = min(min_d, distance_squared(temp[i], temp[j]))
        
        return min_d
    
    return closest_pair(0, len(points) - 1)

def main():
    data = input().strip().split()
    n = int(data[0])
    points = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(n)]
    
    result = closest_pair_of_points(points)
    print(result)

if __name__ == "__main__":
    main()
