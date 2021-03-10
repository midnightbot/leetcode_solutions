class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        
        for x in A:
            if x%2==0:
                ans.append(x)
                
        for y in A:
            if y%2!=0:
                ans.append(y)
                
        return ans
        
