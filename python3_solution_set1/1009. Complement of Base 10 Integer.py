##ss
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        ans = ""
        for x in range(30,-1,-1):
            if n & (1<<x)!=0:
                ans+="1"
                
            else:
                ans+="0"
                
        for x in range(len(ans)):
            if ans[x] == "1":
                break
                
        #print(x,ans)        
        ans = ans[x:]
        #print(ans)
        t = self.find_comp(ans)
        return t
    def find_comp(self,nums):
        ret_ans = ""
        #print(nums)
        for x in range(len(nums)):
            if nums[x] == "1":
                ret_ans+="0"
                
            else:
                ret_ans+="1"
         
        #print(ret_ans)
        thisnum = 0
        ret_ans = ret_ans[::-1]
        for x in range(len(ret_ans)):
            thisnum += pow(2,x) * int(ret_ans[x])
            
        return thisnum
        
        #print(ans)
