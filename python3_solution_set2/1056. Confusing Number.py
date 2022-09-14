class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        n = str(n)
        
        dicts = {0:0 , 1:1 , 6:9 , 8:8 , 9:6}
        invalid = "23457"
        
        for ch in n:
            if ch in invalid:
                return False
            
        ans = ""
        
        for ch in n:
            ans+=str(dicts[int(ch)])
            
        return n!=ans[::-1]
