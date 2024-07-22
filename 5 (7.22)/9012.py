import sys
input = sys.stdin.read

def is_vps(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

def main():
    data = input().strip().split('\n')
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        results.append(is_vps(data[i]))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
