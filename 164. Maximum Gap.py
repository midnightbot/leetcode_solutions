##ss
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        ##linear time sorting -> radix sort (comparing bits of input)
        
        if len(nums) < 2:
            return 0
        
        max_digits = len(str(max(nums)))
        
        ans = self.radixsort(nums,max_digits) ## O(n*len(max number)) i.e O(n*9)
        #print(ans)
        maxs = 0
        for x in range(1,len(ans)):
            maxs = max(maxs,ans[x]-ans[x-1])
            
        return maxs
        
        
    def radixsort(self,nums,max_digits):
        
        for digit in range(0,max_digits):
            B = [[] for x in range(10)]
            
            for item in nums:
                indx = item // 10 ** digit % 10
                B[indx].append(item)
                
                
            nums = self.flatten(B)
            
        return nums
            
    def flatten(self,B):
        ans = []
        for x in range(len(B)):
            for y in range(len(B[x])):
                ans.append(B[x][y])
                
        return ans
        
                
                
