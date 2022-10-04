##Solution 2 using recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.reverse(s,0,len(s)-1)
        
        
    def reverse(self,s,start,end):
        #print("hi",start,end)
        if len(s) == 1:
            return
        
        if start < end:
            s[start],s[end] = s[end],s[start]
            self.reverse(s,start+1,end-1)
        
        
