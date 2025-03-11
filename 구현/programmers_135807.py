import math

def find_gcd(arr):
    # 배열의 모든 원소에 대해 누적하여 최대공약수 구하기
    result = arr[0]
    for num in arr[1:]:
        result = math.gcd(result, num)
    return result

def solution(arrayA, arrayB):
    gcdA = find_gcd(arrayA)
    gcdB = find_gcd(arrayB)

    candidateA = gcdA
    candidateB = gcdB

    for num in arrayB:
        if num % gcdA == 0:
            candidateA = 0
            break

    for num in arrayA:
        if num % gcdB == 0:
            candidateB = 0
            break

    return max(candidateA, candidateB)