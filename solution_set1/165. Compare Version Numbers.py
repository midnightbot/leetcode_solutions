##ss
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        comp1 = version1.split(".")
        comp2 = version2.split(".")
        
        comp1 = [int(x) for x in comp1]
        comp2 = [int(x) for x in comp2]
        
        #print(comp1,comp2)
        if len(comp1) > len(comp2):
            diff = len(comp1) - len(comp2)
            for x in range(diff):
                comp2.append(0)
                
        elif len(comp2) > len(comp1):
            diff = len(comp2) - len(comp1)
            
            for x in range(diff):
                comp1.append(0)
                
                
        for x in range(len(comp1)):
            if comp1[x] == comp2[x]:
                continue
                
            else:
                if comp1[x] > comp2[x]:
                    return 1
                else:
                    return -1
                
        return 0
