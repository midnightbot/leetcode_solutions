##ss
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        ans  = ""
        for x in range(len(num)):
            if num[x] == "0":
                ans+="0"
                
            elif num[x] == "1":
                ans+="1"
                
            elif num[x] in ["2","3","4","5","7"]:
                return False
            
            elif num[x] == "6":
                ans+="9"
                
            elif num[x] == "8":
                ans+="8"
                
            elif num[x] == "9":
                ans+="6"
                
        #print(ans)       
        return ans[::-1] == num
        
