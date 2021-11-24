class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        ans  = []
        
        i = 0
        j = 0
        
        while i<len(firstList) and j<len(secondList):
            
            start = max(firstList[i][0],secondList[j][0])
            end = min(firstList[i][1],secondList[j][1])
            
            if start<=end:
                ans.append([start,end])
                
            if firstList[i][1] < secondList[j][1]:
                i+=1
                
            else:
                j+=1
                
        #print(ans)
        return ans
