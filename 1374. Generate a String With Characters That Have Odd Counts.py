class Solution:
    def generateTheString(self, n: int) -> str:
        strs = ""
        
        if n==1:
            return "a"
        
        elif n%2==0:
            for x in range(n-1):
                strs+= "a"
                
            strs+= "b"
            
            return strs
        
        elif n>=3 and n%2!=0:
            strs +="a"
            for x in range(n-2):
                strs+="b"
                
            strs+="c"
            return strs

        
