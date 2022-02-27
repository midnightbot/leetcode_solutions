##ss
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        ##can delete atmost 1 char
        
        i = 0
        j = len(s) - 1
        
        ans = self.check(i,j,s)
        if ans[0] == True:##already a palindrome
            return True
        
        else:##got 1 mismatch char now check if i+1--> j is palindorme or i->j-1 is palindrome
            ans1 = self.check(ans[1]+1,ans[2],s)
            ans2 = self.check(ans[1],ans[2]-1,s)
            
            if ans1[0] == True or ans2[0] == True:
                return True
            
        return False
        
    def check(self,p1,p2,s):
        
        while p1 <= p2:
            if s[p1]!=s[p2]:
                return False,p1,p2
            p1+=1
            p2-=1
            
        return True,True,True
            
