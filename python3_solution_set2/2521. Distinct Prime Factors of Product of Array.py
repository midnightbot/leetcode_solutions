class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def find_prime_fac(num):
            ans = set()
            c = 2
            while num > 1:
                if num%c==0:
                    ans.add(c)
                    num/=c
                else:
                    c+=1

            return ans  

        a = set()

        for x in nums:
            temp = find_prime_fac(x)

            for it in temp:
                a.add(it)
                 
        return len(a)
