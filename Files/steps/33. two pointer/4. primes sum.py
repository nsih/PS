def two_pointer(n, lst):
    left, right = 0, 0
    current_sum = 0

    cnt = 0

    #오른쪽 포인터를 끝까지 증가시킨다.
    #값이 만족되면 왼쪽포인터를 증가시키고 만족되지 않으면 오른쪽 포인터만 다시 증가시킨다.
    #반복한다.
    while right < len(lst):
        current_sum += lst[right]
        right += 1

        while current_sum >= n:
            if current_sum == n:
                cnt += 1

            current_sum -= lst[left]
            left += 1

    return cnt


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for start in range(2, int(limit ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

import sys

limit = 4000000
primes = sieve_of_eratosthenes(limit)

n = int(sys.stdin.readline())

print(two_pointer(n,primes))