class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        ## binary search approach
        l = min(nums)
        r = max(nums)

        while l < r:
            mid = (l+r)//2
            count = 0
            last_indx = -2

            for i,it in enumerate(nums):
                if i > last_indx + 1:
                    if it <= mid:
                        count+=1
                        last_indx = i

            if count >= k:
                r = mid
            else:
                l = mid + 1

        return l


        ## dynamic programmin approach
        ## TLE
        '''
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        self.result = float('inf')
        n = len(nums)

        memo = {}

        def find_ans(indx, k):
            if (indx,k) in memo:
                return memo[(indx,k)]
            if indx >= n and k == 0:
                return 0

            elif k == 0:
                return 0

            elif indx < n and k > 0:
                memo[(indx,k)] = min(find_ans(indx+1, k), max(find_ans(indx+2,k-1), nums[indx]))
                return memo[(indx,k)]

            else:
                return float('inf')

        find_ans(0,k)
        #print(memo)
        return memo[(0,k)]
        '''
        
