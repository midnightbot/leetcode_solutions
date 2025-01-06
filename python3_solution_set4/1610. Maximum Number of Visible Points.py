class Solution:
    def calculate_angle(self,x1,y1,x2,y2):
        ht = y2-y1
        width = x2-x1
        alpha = math.atan2(ht, width) * (180/math.pi)
        return alpha if alpha >=0 else alpha + 360

    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        ans = 0
        overlap = 0
        arr = []
        for x,y in points:
            if [x,y] == location:
                overlap+=1
            else:
                arr.append(self.calculate_angle(x,y,location[0],location[1]))
        
        
        arr = sorted(arr, key = lambda x:x)
        arr += [x+360 for x in arr]
        i = 0
        j = 0
        n = len(arr)

        while j < n:
            while j < n and arr[j]-arr[i] <= angle:
                j+=1
            
            ans = max(ans, j-i)

            while j < n and i<j and arr[j]-arr[i] > angle:
                i+=1
        
        return ans + overlap
        
