class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        
        
        nums = sorted(nums)
        
        for x in range(len(nums)-2):
            if x==0 or (nums[x-1]!=nums[x]): ##pick any number
                ## find two sum for the following array from index x+1...len(nums)
                low = x + 1
                high = len(nums) - 1
                
                sums = -1 * (nums[x])
                
                ##finding two sum
                while low < high:
                    if nums[low] + nums[high] == sums:
                        ans.add(tuple((nums[x],nums[low],nums[high])))
                        while low < high and nums[low] == nums[low+1]:
                            low+=1
                            
                        while low < high and nums[high] == nums[high-1]:
                            high-=1
                            
                        low+=1
                        high-=1
                        
                    elif nums[low] + nums[high] > sums:
                        high-=1
                        
                    else:
                        low+=1
                        
        return ans
