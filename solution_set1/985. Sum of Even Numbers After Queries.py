##ss
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ans = [0 for x in range(len(queries))]
        
        sums = sum([x for x in nums if x%2==0])
        
        for x in range(len(queries)):
            val = queries[x][0]
            indx = queries[x][1]
            
            if nums[indx] % 2 == 0:
                sums -= nums[indx]
                
            nums[indx]+=val
            if nums[indx] % 2 == 0:
                sums+=nums[indx]
                
            ans[x] = sums
        return ans
        
