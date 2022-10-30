class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        ## maximum of two edits
        
        def find_diff(str1,str2):
            ans = 0
            
            for x in range(len(str1)):
                if str1[x]!=str2[x]:
                    ans+=1
                    
            return ans<=2
        
        
        
        result = []
        
        for x in queries:
            for y in dictionary:
                if find_diff(x,y):
                    result.append(x)
                    break
                    
        return result
        
