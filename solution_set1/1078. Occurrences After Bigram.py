##ss
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        comp = text.split(" ")
        ans = []
        
        for x in range(len(comp)-2):
            if comp[x] == first and comp[x+1] == second:
                ans.append(comp[x+2])
                
        return ans
        
