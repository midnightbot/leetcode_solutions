class Solution:
    def numberOfWeakCharacters(self, prop: List[List[int]]) -> int:
        
        ans = 0
        
        prop = sorted(prop, key = lambda x:(-x[0],x[1]))
        maxs = 0
        for x,y in prop:
            if y < maxs:
                ans+=1
            else:
                maxs = y
        return ans
        
        
