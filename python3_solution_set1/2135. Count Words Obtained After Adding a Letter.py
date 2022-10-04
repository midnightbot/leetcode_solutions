##ss
##Solution1
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        final = []
        
        for x in range(len(startWords)):
            contains = set(startWords[x])
            for y in range(26):
                if chr(97+y) not in contains:
                    temp = startWords[x] + chr(97+y)
                    temp = ''.join(sorted(temp))
                    #print(temp)
                    final.append(temp)
         
        #print(final)
        final = set(final)
        #print(final)
        ans  = 0
        for x in range(len(targetWords)):
            if ''.join(sorted(targetWords[x])) in final:
                ans+=1
                
        return ans
            
        
        
 ##Solution 2
 class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        final = {}
        
        for x in range(len(startWords)):
            contains = set(startWords[x])
            for y in range(26):
                if chr(97+y) not in contains:
                    temp = startWords[x] + chr(97+y)
                    temp = ''.join(sorted(temp))
                    #print(temp)
                    final[temp] = 1
         
        #print(final)
        
        #print(final)
        ans  = 0
        for x in range(len(targetWords)):
            if ''.join(sorted(targetWords[x])) in final:
                ans+=1
                
        return ans
            
        
