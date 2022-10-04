##ss
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        count = 0
        
        
        def prefix(str1,str2):
            
            if len(str2) < len(str1):
                return False
            
            for x in range(len(str1)):
                if str1[x]!=str2[x]:
                    return False
                
            return True
        
        
        for x in words:
            if prefix(x,s):
                count+=1
                
        return count
        
