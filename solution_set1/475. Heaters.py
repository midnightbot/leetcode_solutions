##ss
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        result = [float('inf') for x in range(len(houses))]
        houses = sorted(houses)
        heaters = sorted(heaters)
        for x in range(len(houses)):
            
            left = 0
            right = len(heaters) - 1
            
            while left <= right:
                mid = left +(right - left) // 2
                
                if abs(heaters[mid] - houses[x]) < result[x]:
                    result[x] = abs(heaters[mid] - houses[x])
                    
                if heaters[mid] > houses[x]:
                    right = mid - 1
                    
                else:
                    left = mid + 1
                    
        return max(result)
                
        
        
        
