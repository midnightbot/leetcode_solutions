class Solution:
    def evenProduct(self, nums: List[int]) -> int:

        ## number of arrays having atleast one even element

        ans = 0
        n = len(nums)
        points = []

        for x in range(len(nums)):
            if nums[x]%2==0:
                points.append(x)

        
        i = 0
        if i == len(points):
            return 0
                    
        for x in range(n):
            #print(x, i, points)
            if points[i] == x:
                ans+=(n-points[i])
                i+=1
                if i == len(points):
                    break
            else:
                ans+=(n-points[i])

        return ans
