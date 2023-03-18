class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        ## simple greedy iteration
        n= len(warehouse)
        low = 0
        high = n-1

        boxes = sorted(boxes, reverse = True)
        ans = 0
        for x in range(len(boxes)):
            if low <= high:
                if boxes[x] <= warehouse[low]:
                    low+=1
                    ans+=1

                elif boxes[x] <= warehouse[high]:
                    high-=1
                    ans+=1

        return ans
        
