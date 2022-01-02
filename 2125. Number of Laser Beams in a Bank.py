##ss
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        temp = []
        
        for x in range(len(bank)):
            counts = bank[x].count("1")
            if counts!=0:
                temp.append(counts)
         
        #print(temp)
        if len(temp) == 0:
            return 0
        
        ans = 0
        for x in range(len(temp)-1):
            ans+=temp[x] * temp[x+1]
            
        return ans
        
        
        
