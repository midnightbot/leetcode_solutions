##ss
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ##s1 desc s2 desc
        ## or s1 desc and s1 desc
        ## try both
        
        def check_con(s1,s2):
            #print(s1,s2)
            for x in range(len(s1)):
                if ord(s1[x]) >= ord(s2[x]):
                    continue
                else:
                    return False

            return True
        
        comp1 = sorted(s1)
        comp2 = sorted(s1,reverse = True)
        comp3 = sorted(s2)
        comp4 = sorted(s2, reverse = True)
        
        return check_con(comp4,comp2) or check_con(comp2,comp4)
        
    
        
        
