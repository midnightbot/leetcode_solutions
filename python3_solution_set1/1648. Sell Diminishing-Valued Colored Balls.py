import heapq
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        mods = 10**9 + 7
        inventory = sorted(inventory, reverse = True)
        inventory.append(0)
        
        result = 0
        grp_size = 1
        
        for x in range(len(inventory)-1):
            if inventory[x] > inventory[x+1]:
                
                if grp_size * (inventory[x] - inventory[x+1]) < orders:
                    elems = inventory[x] - inventory[x+1]
                    
                    result+= grp_size * (inventory[x] + inventory[x+1] + 1) * (elems)//2
                    orders-= grp_size * elems
                    
                    
                else:
                    q,r = divmod(orders,grp_size)
                    result+= grp_size * (inventory[x] + (inventory[x]-q+1)) * (q)//2
                    result+= r * (inventory[x] - q)
                    result%=mods
                    return result
                
                    
            grp_size+=1
                
        
        
