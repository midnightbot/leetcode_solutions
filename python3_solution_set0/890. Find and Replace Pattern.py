##SS
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        compare = [1]
        maxs = 1
        for x in range(1,len(pattern)):
            if pattern[x] in pattern[0:x]:
                indx = pattern[0:x].index(pattern[x])
                compare.append(compare[indx])
             
            else:
                maxs+=1
                compare.append(maxs)
                
        print(compare)
        ans  = []
        for x in range(len(words)):
            if self.find_pattern(words[x]) == compare:
                ans.append(words[x])
        return ans
            
     
    def find_pattern(self,pattern):
        compare = [1]
        maxs = 1
        for x in range(1,len(pattern)):
            if pattern[x] in pattern[0:x]:
                indx = pattern[0:x].index(pattern[x])
                compare.append(compare[indx])
             
            else:
                maxs+=1
                compare.append(maxs)
                
        return compare
        
