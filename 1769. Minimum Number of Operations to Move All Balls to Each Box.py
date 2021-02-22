class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans =[]
        count = 0
        for x in range(len(boxes)):
            count = 0
            for y in range(len(boxes)):
                if(x!=y and boxes[y]=="1"):
                    
                    count = count + (abs(y-x))
                
            ans.append(count)
        return ans
                
        
