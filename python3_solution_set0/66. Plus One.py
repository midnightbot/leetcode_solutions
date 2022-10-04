class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = [str(i) for i in digits]
        
        res = int("".join(s))
        res+=1
        
        ans = [int(x) for x in str(res)]
        return ans
        #print(res)
        
