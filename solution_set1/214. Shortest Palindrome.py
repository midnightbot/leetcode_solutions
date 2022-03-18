##ss
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        ## add characters in front of s to make it a palindrome
        
        ## max string size will be 2 * len(s)
        
        
        def palindrome(i,j):
            #print(i,j)
            if i < len(s) and j >=0 and i< j and s[i] == s[j]:
                i+=1
                j-=1
                return palindrome(i,j)
                
            elif i == j or i > j:
                return True
            
            else:
                return False
            
            return True
        
     
        loc = -1
        for x in range(len(s)):
            #print(s[0:len(s)-x])
            if s[0:len(s)-x] == s[0:len(s)-x][::-1]:
                loc = x
                break
        
        
        #print(loc)
        if loc!=-1:
            temp = ""
            for x in range(loc):
                temp+=s[-x-1]


            return temp + s
        
        else:
            return s[::-1][0:-1] + s
            
        
