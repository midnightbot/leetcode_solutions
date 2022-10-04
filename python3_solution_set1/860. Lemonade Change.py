##ss
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = [0,0,0]
        
        for x in bills:
            
            if x == 5:
                change[0]+=1
                
            elif x==10:
                if change[0]==0:
                    return False
                
                else:
                    change[1]+=1
                    change[0]-=1
                    
            elif x==20:
                if change[1] == 0:
                    if change[0] < 3:
                        return False
                
                    else:
                        change[0]-=3
                        change[2]+=1
                        
                else:
                    if change[0] == 0:
                        return False
                    
                    else:
                        change[0]-=1
                        change[1]-=1
                        change[2]+=1
                        
        return True
        
