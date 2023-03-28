class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ## [1,1,2,2,3,7]
        
        ## always move a repeating number to smallest non occuring number

        ## maintain a counter of seen elements and find the smallest not seen element
        
        ans = 0
        global_seen = set(nums)
        i = 1
        nums = sorted(nums)
        local_seen = set()

        for x in nums:
            if x not in local_seen:
                local_seen.add(x)

            else:
                while i in global_seen or i <= x:
                    i+=1
                #print(i,x)
                ans+=(i-x)
                global_seen.add(i)

        return ans
