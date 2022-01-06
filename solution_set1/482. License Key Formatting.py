##ss
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.upper()
        temp = s.split("-")
        #print(temp)
        #temp = temp[::-1]
        result = ""
        thisans = ""
        for x in range(len(temp)-1,-1,-1):
            for y in range(len(temp[x])-1,-1,-1):
                if len(thisans)!=k:
                    thisans+=temp[x][y]
                    
                else:
                    result+=thisans
                    result+="-"
                    thisans = temp[x][y]
                    
                    
        result+=thisans
        return result[::-1]
        
        
        
