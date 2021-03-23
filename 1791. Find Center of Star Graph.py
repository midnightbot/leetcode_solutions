class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        ans = []
        
        for x in range(len(edges)):
            ans.append(edges[x][0])
            ans.append(edges[x][1])
            
        count1 = ans.count(ans[0])
        count2 = ans.count(ans[1])
        
        if count1 == int(len(ans)/2):
            return ans[0]
        else:
            return ans[1]
        
