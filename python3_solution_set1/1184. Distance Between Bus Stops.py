##ss
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans = 0
        arr = [start,destination]
        start = min(arr)
        destination = max(arr)
        for x in range(start,destination):
            ans+=distance[x]
            
        return min(ans, sum(distance)-ans)
        
