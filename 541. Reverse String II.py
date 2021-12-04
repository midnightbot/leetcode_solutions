class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        a = list(s)
        for x in range(0,len(a),2*k):
            a[x:x+k] = reversed(a[x:x+k])
            
        return "".join(a)
        
