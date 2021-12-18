###ss
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ans = []
        
        
        not_present = [x for x in range(n+1)]
        
        for x in range(len(target)):
            not_present[target[x]] = 0
            
        not_there = set(not_present)
        not_there.remove(0)
        
        print(not_there)
        
        if len(not_there)!=0 and min(not_there) > max(target):
            for x in range(len(target)):
                ans.append("Push")
                
            return ans
        for x in range(1,min(n+1,max(target)+1)):
            if x in not_there:
                ans.append("Push")
                ans.append("Pop")
                
            else:
                ans.append("Push")
                
        return ans
