class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        else:
            res = [int(u) for u in str(x)]
            #print(res)
            
            temp = res[::-1]
            for x in range(len(res)):
                if res[x]!=temp[x]:
                    return False
                
                
            return True
