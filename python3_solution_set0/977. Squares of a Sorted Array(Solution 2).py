class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if nums[0] >=0:
            ans = [x**2 for x in nums]
            return ans
        
        elif nums[len(nums)-1] <=0:
            ans = [x**2 for x in nums]
            return ans[::-1]
                
        else:
            index = -1
            for x in range(len(nums)):
                if nums[x] > 0:
                    index = x
                    break
            ans1 = [x**2 for x in nums[0:index]]
            ans2 = [x**2 for x in nums[index:len(nums)]]
            ans1 = ans1[::-1]
            c1 = 0
            c2 = 0
            ans = []
            while c1!=len(ans1) and c2!=len(ans2):
                if ans1[c1] < ans2[c2]:
                    ans.append(ans1[c1])
                    c1+=1
                    
                else:
                    ans.append(ans2[c2])
                    c2+=1
                    
            while c1!=len(ans1):
                ans.append(ans1[c1])
                c1+=1
                
            while c2!=len(ans2):
                ans.append(ans2[c2])
                c2+=1
                
            return ans
                
                
        
