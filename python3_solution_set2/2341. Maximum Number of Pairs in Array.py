##ss
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        temp = Counter(nums)
        ans = [0,0]
        
        for x in temp:
            ans[0]+=temp[x]//2
            
        ans[1] = len(nums) - ans[0]*2
        
        return ans
        
