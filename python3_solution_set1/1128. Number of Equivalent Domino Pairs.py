##ss
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        
        dicts = {}
        for it,(x,y) in enumerate(dominoes):
            if (x,y) in dicts:
                dicts[(x,y)].add(it)
            else:
                dicts[(x,y)] = {it}
                
            if (y,x) in dicts:
                dicts[(y,x)].add(it)
                
            else:
                dicts[(y,x)] = {it}
                
        for it,(x,y) in enumerate(dominoes):
            temp = [c>it for c in list(dicts[(x,y)].union(dicts[(y,x)]))]
            ans+=sum(temp)
            
        return ans
