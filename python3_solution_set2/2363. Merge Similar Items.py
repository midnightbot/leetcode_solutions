class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        temp = {}
        for x,y in items1:
            temp[x] = y
            
        for x,y in items2:
            if x in temp:
                temp[x]+=y
            else:
                temp[x] = y
                
                
        ans = []
        for x in temp:
            ans.append([x,temp[x]])
            
        ans = sorted(ans, key = lambda x:x[0])
        return ans
