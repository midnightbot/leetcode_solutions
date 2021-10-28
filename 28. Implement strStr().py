class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        counter = 0
        for x in range(len(haystack)):
            if haystack[x:x+len(needle)] == needle:
                return x

                
                
        return -1
                    
        
