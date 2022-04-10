##ss
class Solution:
    def largestInteger(self, num: int) -> int:
        
        nums = str(num)
        epos = []
        opos = []
        e = []
        o = []
        nums = [int(x) for x in nums]
        for x in range(len(nums)):
            if nums[x]%2 == 0:
                e.append(nums[x])
                epos.append(x)
                
            else:
                o.append(nums[x])
                opos.append(x)
                
        e = sorted(e,reverse = True)
        o = sorted(o, reverse = True)
        
        ans = [-1 for x in range(len(nums))]
        
        i = 0
        for x in range(len(epos)):
            ans[epos[x]] = e[i]
            i+=1
            
        i = 0
        
        for x in range(len(opos)):
            ans[opos[x]] = o[i]
            i+=1
            
        ans = [str(x) for x in ans]
        return int("".join(ans))
                
        
