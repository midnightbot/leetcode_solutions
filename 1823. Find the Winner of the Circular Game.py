class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        ans  = []
        for x in range(n):
            ans.append(x+1)
            
        print(ans)
        
        start = 0
        for y in range(n-1): # as to select only one winner
            temp = (start + k - 1)%len(ans)
            removing_element = ans[temp]
            next_element = ans[(temp+1)%(len(ans))]
            ans.remove(removing_element)
            #print(ans)
            start = ans.index(next_element)
            
        return ans[0]
