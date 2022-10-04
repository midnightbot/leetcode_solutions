##ss
class Solution:
    def trap(self, height: List[int]) -> int:
        
        lmax = height[0]
        #ans = [0 for x in range(len(height))]
        water = 0
        for x in range(1,len(height)-1):
            rmax = max(height[x+1:len(height)])
            
            if height[x] < min(rmax,lmax):
                water+= min(rmax,lmax) - height[x]
                
            lmax = max(lmax,height[x])
            
            
        return water
                
        
