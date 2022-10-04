##ss
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        ## L>=W
        ## min abs(L-W)
        
        
        for x in range(int(math.sqrt(area))+1,-1,-1):
            
            y = area / x
            temps = area // x
            
            if y == temps:
                return [max(temps,x),min(temps,x)]
