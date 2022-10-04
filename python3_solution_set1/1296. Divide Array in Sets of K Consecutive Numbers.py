##ss
##same as 846. Hand of Straights

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        nums = sorted(nums)
        dicts = {}
        keys = 0
        for x in range(len(nums)):
            if nums[x] in dicts:
                dicts[nums[x]]+=1
                
            else:
                keys+=1
                dicts[nums[x]] = 1
                
        while dicts:
            count = 0
            #print(dicts)
            done = False
            if keys < k:
                return False
            for x in dicts:
                if count == k:
                    done = True
                    break
                if count == 0:
                    prev = x
                    
                else:
                    if x!=prev+1:
                        return False
                    
                    prev = x
                    
                count+=1
                
            if count == k:
                done = True
                
            if done == True:
                count = 0
                remove = []
                for x in dicts:
                    if count == k:
                        break
                        
                    dicts[x]-=1
                    if dicts[x] == 0:
                        remove.append(x)
                        
                    count+=1
                for x in range(len(remove)):
                    keys-=1
                    dicts.pop(remove[x])
                    
        return True
        
