##ss
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        def converter(word):
            ans = [0 for x in range(26)]
            
            for x in word:
                ans[ord(x)-ord('a')]+=1
                
            return ans
        
        
        needed = [0 for x in range(26)]
        
        
        for x in words2:
            res = converter(x)
            needed = [max(needed[x],res[x]) for x in range(26)]
            
        def comp(arr1,arr2):
            for x in range(26):
                if arr2[x] < arr1[x]:
                    return False
            return True
        
        ret = []
        
        for x in words1:
            if comp(needed, converter(x)):
                ret.append(x)
        
        return ret
        
