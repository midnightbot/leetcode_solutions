class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        def find_subarray_ans(arr):
            ans = 0
            for x in arr:
                ans|=x
            return ans

        maxs = find_subarray_ans(nums)  ## max bitwise or is bitwise or of entire array

        n = len(nums)
        res = [0]

        ## finding all subarrays
        def find_subarrays(indx, arr):
            if indx == n:
                if find_subarray_ans(arr) == maxs:
                    #print('here')
                    res[0]+=1

            else:
                find_subarrays(indx+1, arr)
                find_subarrays(indx+1, arr + [nums[indx]])

        find_subarrays(0, [])
        
        return res[0]
