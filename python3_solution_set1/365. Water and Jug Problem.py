##ss
class Solution:
    def canMeasureWater(self, j1: int, j2: int, cap: int) -> bool:
        
        if j1 + j2 < cap:
            return False
        
        visited = set()
        q = [(0,0)]
        
        while q:
            c1,c2 = q.pop(0)
            if c1 + c2 == cap:
                return True
            
            else:
                temp = []
                temp.append((j1,c2))##fill jar1
                temp.append((c1,j2)) ## fil jar2
                temp.append((0,c2))## empty jar1
                temp.append((c1,0)) ## empty jar2
                
                if c1 + c2 <= j2: ##pour jar1 into jar2
                    temp.append((0,c1+c2))
                    
                else:
                    temp.append((c1-(j2-c2), j2))
            
            
                if c1 + c2 <= j1: ## pour jar2 into jar1
                    temp.append((c1+c2,0))
                    
                else:
                    temp.append((j1, c2 - (j1- c1)))
                    
                
                for x in temp:
                    if x not in visited:
                        visited.add(x)
                        q.append(x)
                        
                        
        return False
