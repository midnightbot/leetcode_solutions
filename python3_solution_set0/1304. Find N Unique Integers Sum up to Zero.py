class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        
        if n==1:
            ans.append(0)
            return ans
        
        elif n%2!=0:
            temp = -(n-2)
            for x in range(temp, -temp+2, 2):
                ans.append(x)
                
            ans.append(0)
            return ans
        
        else:
            temp = -(n-1)
            for x in range(temp, -temp+1, 2):
                ans.append(x)
                
            return ans
