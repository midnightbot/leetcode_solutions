class Solution:
    def stableMountains(self, height: List[int], t: int) -> List[int]:
        ans = []

        for x in range(1, len(height)):
            if height[x-1] > t:
                ans.append(x)
        return ans
        
