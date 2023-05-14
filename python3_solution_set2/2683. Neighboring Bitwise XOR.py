class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ## either first element will be 0 or 1
        ## try both and see if a valid sequence could be found
        done1 = False
        done2 = False
        ## first element is 0
        derived = derived + [derived[0]]
        ele = 0
        for x in range(len(derived)-1):
            if derived[x]==1:
                ele+=1
                ele%=2

        if ele == 0:
            done1 = True
        
        ## first element is 1
        ele = 1
        for x in range(len(derived)-1):
            if derived[x]==1:
                ele+=1
                ele%=2

        if ele == 1:
            done2 = True

        return done1 or done2
