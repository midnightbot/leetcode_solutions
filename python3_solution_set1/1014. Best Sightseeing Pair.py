##ss
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ## for i in range(n) for j in range(i+1,n) maximize: v[j] + v[i] + (i - j )
        temp = [values[-1] - len(values) + 1]
        
        for x in range(len(values) - 2, -1,-1):
            temp.append(max(temp[-1], values[x] - x))
            
        temp = temp[::-1]
        ans  = 0
        for x in range(len(values) -1):
            ans = max(ans , values[x] + x + temp[x+1])
            
        return ans
        
        
