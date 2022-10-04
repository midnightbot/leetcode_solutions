##ss
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        def find_sum(strs):
            return str(sum([int(x) for x in strs]))
        
        while len(s) > k:
            new_s = ""
            temp = len(s) % k
            div = len(s) // k
            for x in range(div):
                new_s+= find_sum(s[x*k:x*k+k])
                
             
            if temp!=0:
                new_s+= find_sum(s[-temp:])
            
            #print(new_s)
            s = new_s
            
        return s
