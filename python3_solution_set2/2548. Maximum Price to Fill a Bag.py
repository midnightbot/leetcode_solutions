class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:

        items = [[x[0],x[1],x[0]/x[1]] for x in items]
        
        items = sorted(items, reverse=True, key = lambda x:x[2])
        price = 0
        i = 0
        while capacity>0 and i < len(items):
            if items[i][1] <= capacity:
                price+=items[i][0]
                capacity-=items[i][1]
            else:
                ratio = capacity / items[i][1]
                price+= ratio * items[i][0]
                capacity=0
            i+=1
        return price if capacity==0 else -1
