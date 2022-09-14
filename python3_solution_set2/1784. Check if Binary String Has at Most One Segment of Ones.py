class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        total_count = 0
        
        this_count = 0
        
        for x in s:
            if x == '1':
                this_count+=1
                
            elif x == '0' and this_count!=0:
                total_count+=1
                this_count = 0
                
        if this_count>0:
            total_count+=1
        return total_count <= 1
        
