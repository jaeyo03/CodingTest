import heapq

def solution(n, k, enemy):
    max_heap = []
    for i in range(len(enemy)):
        # Add the enemy count to the max heap (as a negative number)
        heapq.heappush(max_heap, -enemy[i])
        n -= enemy[i]  # Subtract the enemy count from soldiers
        if n >= 0:
            continue
        if k > 0:
            # Use invincibility on the largest enemy count encountered so far
            largest_enemy = -heapq.heappop(max_heap)
            n += largest_enemy  # Restore soldiers
            k -= 1
        else:
            # Can't proceed further, return rounds survived so far
            return i
    # Survived all rounds
    return len(enemy)
