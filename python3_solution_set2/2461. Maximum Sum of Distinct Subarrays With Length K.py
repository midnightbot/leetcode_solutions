class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        ## simple sliding window
        ## maintain count of each element in the window
        ## maintain count of unique elements in this window
        ## maintain sum of elements in this window
        ## check if number of unique elements in this window is K update ans = max(ans, sum_of_this_window)
        size = 0
        seen = {}
        sums = 0
        ans = 0
        for x in range(k):
            if nums[x] in seen:
                seen[nums[x]]+=1
                sums+=nums[x]
            else:
                seen[nums[x]] = 1
                size+=1
                sums+=nums[x]

        for x in range(k, len(nums)):
            if size == k:
                ans = max(ans, sums)

            seen[nums[x-k]]-=1
            sums-=nums[x-k]
            if seen[nums[x-k]] == 0:
                seen.pop(nums[x-k])
                size-=1

            if nums[x] in seen:
                seen[nums[x]]+=1
                sums+=nums[x]
            
            if nums[x] not in seen:
                seen[nums[x]] = 1
                sums+=nums[x]
                size+=1
            

            
        if size == k:
            ans = max(ans, sums)
        return ans
        
