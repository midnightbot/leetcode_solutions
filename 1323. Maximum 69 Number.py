class Solution:
    def maximum69Number (self, num: int) -> int:
        
        res = [int(x) for x in str(num)] 
        
        for y in range(len(res)):
            if res[y]==6:
                res[y]=9
                break
        s = [str(i) for i in res]
        
        ans = int("".join(s))
        return ans
