##ss
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        c = Counter(deck)
        
        for x in range(2,len(deck)+1):
            if all(c[v]%x == 0 for v in c):
                return True
            
        return False
        
