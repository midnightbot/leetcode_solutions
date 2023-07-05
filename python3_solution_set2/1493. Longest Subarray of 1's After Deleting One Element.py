class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        prev_count = 0
        temp = []

        for x in range(len(nums)):
            if nums[x] == 0:
                if prev_count!=0:
                    temp.append(prev_count)
                    prev_count = 0
                temp.append(0)
            else:
                prev_count+=1

        if prev_count!=0:
            temp.append(prev_count)

        ## now iterate over temp
        ## and find sum of subarrays of size3
        ## if they have 0 then sum + 1 if no zero then sum-min(subarray)
        ans = 0
        n = len(temp)
        if len(temp) == 1:
            if temp[0] >0:
                return temp[0]-1
            else:
                return 0

        elif len(temp) == 2:
            return max(temp) 

        for x in range(n-2):
            arr = temp[x:x+3]
            ## if arr has no 0
            if arr.count(0) == 0:
                ans = max(ans, sum(arr)-1)
            ## arr has one 0 or two 0 or three 0
            else:
                ans = max(ans, sum(arr))
        return ans
