class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans = []
        sorted_array=[]
        for x in range(len(l)):
            sorted_array.clear()
            for y in range(l[x],r[x]+1,1):
                sorted_array.append(nums[y])
                
                
            sorted_array = sorted(sorted_array)
            z=0
            counter = 0
            temp = 0
            for z in range(len(sorted_array)-1):
                
                if sorted_array[z+1]-sorted_array[z]!=sorted_array[1]-sorted_array[0]:
                    ans.append(False)
                    break
                else:
                    counter+=1
                
                
                
                if counter==int(len(sorted_array)-1):
                    ans.append(True)
                    break
        return ans
                
                
                
        
