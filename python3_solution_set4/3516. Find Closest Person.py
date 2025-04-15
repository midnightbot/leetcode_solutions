class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x-z)
        dist2 = abs(y-z)

        if dist1 > dist2:
            return 2
        elif dist1 < dist2:
            return 1
        else:
            return 0
        
