class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        primes = []

        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        return len(primes)
        