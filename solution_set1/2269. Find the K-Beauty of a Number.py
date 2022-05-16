##ss
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        count = 0
        
        num = str(num)
        
        for x in range(len(num)-k+1):
            temp = num[x:x+k]
            
            if int(temp)!=0 and int(num) % int(temp) == 0:
                count+=1
                
        return count
        
