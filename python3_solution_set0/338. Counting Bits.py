class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ans = []
        for x in range(num+1):
            #ans.append(x)
            temp =x
            count = 0
            while(temp):
                count +=temp &1
                temp>>=1
            ans.append(count)
            
        return ans
        
