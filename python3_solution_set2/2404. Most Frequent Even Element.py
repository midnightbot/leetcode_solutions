class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        temp = Counter(nums)
        ans = -1
        vals = -1
        for x in temp:
            if x%2==0 and vals < temp[x]:
                vals = temp[x]
                ans = x
                
            elif x%2==0 and vals == temp[x]:
                ans = min(ans, x)
                
        return ans
