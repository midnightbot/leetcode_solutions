class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        mins  = warehouse[0]
        
        for x in range(1,len(warehouse)):
            mins = min(mins, warehouse[x])
            warehouse[x] = mins
            
        # print(warehouse)
        # now find box with closest warehouse size
        
        warehouse = sorted(warehouse)
        
        boxes = sorted(boxes)
        c = 0
        it = 0
        #print(warehouse)
        #print(boxes)
        for x in range(len(boxes)):
            while it < len(warehouse) and warehouse[it] < boxes[x]:
                it+=1
                
            
            if it < len(warehouse):
                c+=1
                it+=1

        return c
