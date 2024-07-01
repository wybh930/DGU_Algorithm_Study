def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

N = int(input().strip())
numbers = list(map(int, input().strip().split()))


prime_count = 0

for number in numbers:
    if is_prime(number):
        prime_count += 1
print(prime_count)
