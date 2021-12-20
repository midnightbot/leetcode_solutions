##ss
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes, reverse = True, key = lambda x:(x[1]))
        ans = 0
        for x in range(len(boxTypes)):
            #print(ans,truckSize)
            if boxTypes[x][0] < truckSize:
                ans+= boxTypes[x][0] * boxTypes[x][1]
                truckSize-= boxTypes[x][0]
                
            else:
                ans += truckSize * boxTypes[x][1]
                break
                
        return ans
        
