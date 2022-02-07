##ss
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        left = ""
        comp = ["10","11","0"]
        for x in range(len(bits)-1):
            if left in comp:
                left = ""
                left+=str(bits[x])
                
            else:
                left+=str(bits[x])
                
        if left in comp:
            left = ""
            
        return left == ""
        
