class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        thismask = 0
        ans = 0
        
        for x in range(32,-1,-1):
            
            
            thismask = thismask | 1 << x
            print(thismask,"mask")
            ##100
            thisset = set([thismask & y for y in nums])
            ##thisset = 100
            print(thisset,"set")
            temp = ans | 1<<x
            print(temp,"temp")
            for y in thisset:
                print(y^temp,"steps")
                if y^temp in thisset:
                    ans = temp
                    
        return ans
        
