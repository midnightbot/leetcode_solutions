##ss
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        dict1 = {}
        dict2 = {}
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            return 0
        for x in range(0,len(nums),2):
            if nums[x] in dict1:
                dict1[nums[x]]+=1
            else:
                dict1[nums[x]] = 1
                
            if x+1 < len(nums):   
                if nums[x+1] in dict2:
                    dict2[nums[x+1]]+=1

                else:
                    dict2[nums[x+1]] = 1
                
                
        comp1 = []
        comp2 = []
        
        for x in dict1:
            comp1.append([dict1[x],x])
            
        for x in dict2:
            comp2.append([dict2[x],x])
            
        #print(comp1,comp2)
        comp1 = sorted(comp1, reverse = True, key = lambda x:x[0])
        comp2 = sorted(comp2,reverse = True, key = lambda x:x[0])
        
        #print(comp1,comp2)
        if comp1[0][1]!=comp2[0][1]:
            return len(nums) - comp1[0][0] - comp2[0][0]
        
        else:
            if len(comp1)>=2 and len(comp2)>=2:
                return len(nums) - max(comp1[0][0]+comp2[1][0],comp1[1][0]+comp2[0][0])
            
            elif len(comp2) == 1 and len(comp1)>=2:
                if comp2[0][1] == comp1[0][1]:
                    return len(nums) - comp1[1][0] - comp2[0][0]
                
                else:
                    return len(nums) - comp1[0][0] - comp2[0][0]
                
            elif len(comp1) == 1 and len(comp2) == 1:
                if comp1[0][1] == comp2[0][1]:
                    return len(nums)//2
                else:
                    return len(nums) - comp1[0][0] - comp2[0][0]
                
            elif len(comp1) ==1 and len(comp2)>=2:
                if comp1[0][1] == comp2[0][1]:
                    return len(nums) - comp1[0][0] - comp2[1][0]
                
                else:
                    return len(nums) - comp1[0][0] - comp2[0][0]
        #while ans == False:
            
            
