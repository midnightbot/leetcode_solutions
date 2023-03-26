from bisect import bisect_left, bisect_right
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        ## start iterating nums in reverse order
        ## if nums[i] > nums[i+1] then subtract the smallest prime number greater than nums[i+1] - nums[i]

        def generate_prime(n):
            is_prime = [True] * (n+1)
            is_prime[0] = is_prime[1] = False
            for p in range(2, int(n**0.5)+1):
                if is_prime[p]:
                    for i in range(p*p, n+1, p):
                        is_prime[i] = False
            
            ans= []
            for x in range(2,n+1):
                if is_prime[x]:
                    ans.append(x)

            return ans

        
        primes = generate_prime(2000)
        #print(primes)
        for x in range(len(nums)-2,-1,-1):
            if nums[x] < nums[x+1]:
                continue

            else:
                reduce = (nums[x] - nums[x+1]) + 1
                if reduce >= 1000:
                    return False
                indx = bisect_left(primes, reduce)
                print(indx, reduce)
                nums[x]-=primes[indx]

        for x in range(1, len(nums)):
            if nums[x] <= nums[x-1] or nums[x] <=0:
                return False
        #print(nums)
        return nums[0]>0


