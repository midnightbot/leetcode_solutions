##ss
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        ans = ""
        
        for x in range(len(s)):
           
            if (ord(s[x])>=97 and ord(s[x])<=122) or(ord(s[x])>=48 and ord(s[x])<=57):
                ans+=s[x]
                
       
        return ans == ans[::-1]
        
