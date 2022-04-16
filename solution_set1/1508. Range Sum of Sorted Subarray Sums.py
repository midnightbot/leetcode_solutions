##ss
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mods = 10 **9 + 7
        
        pre = [0]
        
        for x in nums:
            pre.append(pre[-1] + x)
            
        comp = []
        for x in range(1,len(pre)):
            for y in range(x-1,-1,-1):
                comp.append(pre[x] - pre[y])
                
        comp = sorted(comp)
        
        return sum(comp[left-1:right]) % mods
        
