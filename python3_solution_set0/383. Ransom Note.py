class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #a = [str(x) for x in ransomNote]
        b = [str(x) for x in magazine]
        
        for x in range(len(ransomNote)):
            if ransomNote[x] not in b:
                return False
            else:
                b.remove(ransomNote[x])
                
        return True
        
