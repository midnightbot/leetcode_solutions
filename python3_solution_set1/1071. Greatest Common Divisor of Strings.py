##ss
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        ans = 0
        
        for x in range(1,min(len(str1), len(str2))+1):
            
            temp1 = str1[:x]
            temp2 = str2[:x]
            
            a = len(str1) // len(temp1)
            b = len(str2) // len(temp2)
            
            if len(str1) % len(temp1) == 0 and "".join([temp1 for x in range(a)]) == str1 and len(str2) % len(temp2) == 0 and "".join([temp2 for x in range(b)]) == str2 and temp1 == temp2:
                ans = temp1
                
            #print(temp1, a, "".join([temp1 for x in range(a)]))
        return ans if ans!=0 else ""
            
        
        
        
