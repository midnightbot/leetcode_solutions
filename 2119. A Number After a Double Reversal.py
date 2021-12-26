##ss
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if num == 0:
            return True
        
        #print(int(str(num)[len(str(num))-1]))
        return  int(str(num)[len(str(num))-1]) != 0
        
