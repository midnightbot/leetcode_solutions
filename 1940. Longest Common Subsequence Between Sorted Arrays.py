##ss
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        
        ans = set(arrays[0])
        
        for x in range(len(arrays)):
            ans = ans.intersection(arrays[x])
         
        ans = sorted(ans)
        return ans
        
