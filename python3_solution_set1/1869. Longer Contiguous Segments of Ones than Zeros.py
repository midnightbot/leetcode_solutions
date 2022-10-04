##ss
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        ones = -1
        zeros = -1
        
        count = 1
        prev = s[0]
        for x in range(1,len(s)):
            if s[x] == prev:
                count+=1
                
            else:
                if prev == "0":
                    zeros = max(zeros,count)
                    
                else:
                    ones = max(ones,count)
                    
                prev = s[x]
                count = 1
                
        if prev == "0":
            zeros = max(zeros,count)
            
        else:
            ones = max(ones,count)
 
        #print(ones,zeros)        
        return ones > zeros
