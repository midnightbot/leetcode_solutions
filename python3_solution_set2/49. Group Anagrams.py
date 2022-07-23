##ss
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        maps = {}
        
        for x in strs:
            temp = "".join(sorted(x))
            if temp in maps:
                maps[temp].append(x)
            else:
                maps[temp] = [x]
                
        ans = []
        
        for x in maps:
            ans.append(maps[x])
            
        return ans
