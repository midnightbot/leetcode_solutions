##ss
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        hills = 0
        valleys = 0
        
        prev = nums[0]
        arr = []
        for x in range(len(nums)):
            if nums[x] == prev:
                continue
                
            else:
                arr.append(prev)
                prev = nums[x]
        
        arr.append(prev)
        
        
        for x in range(1,len(arr)-1):
            temp1 = -1
            temp2 = -1
            for a in range(x-1,-1,-1):
                if arr[a]!=arr[x]:
                    temp1 = arr[a]
                    break
                    
            for b in range(x+1,len(arr)):
                if arr[b]!=arr[x]:
                    temp2 = arr[b]
                    break
                    
            if temp1!=-1 and temp2!=-1:
                
                if temp1 < arr[x] and temp2 < arr[x]:
                    hills+=1
                    
                elif temp1 > arr[x] and temp2 > arr[x]:
                    valleys+=1
                    
        return hills+valleys
