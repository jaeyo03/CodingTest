from itertools import permutations
from math import sqrt

# 시간복잡도 O(N) 인 소수 찾기
def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

        if count > 2:
            return False

    return True

# 제곱수 까지 하는 소수 찾기
def sqrt_is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1): # +1까지 한걸로 가야함, 나는 sqrt숫자까지만 했음
        if number % i == 0:
            return False
    return True

# 제일 빠른 소수 찾기
def better_is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # sqrt(n)까지 반복하며 확인
    for i in range(5, int(sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    nums_set = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = "".join(p)
            num = int(num)
            nums_set.add(num)

    for n in nums_set:
        if n == 1 or n == 0:
            continue

        if is_prime(n):
            answer += 1

    return answer