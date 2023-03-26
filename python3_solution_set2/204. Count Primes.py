class Solution:
    def countPrimes(self, n: int) -> int:
        ## Sieve of Eratosthenes Algorithm
        if n <= 1:
            return 0
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5)+1):
            if is_prime[p]:
                for i in range(p*p, n+1, p):
                    is_prime[i] = False
        
        ans = 0
        for x in range(2,n):
            if is_prime[x]:
                ans+=1

        return ans
