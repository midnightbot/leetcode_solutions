##ss
class Solution:
    def shortestCompletingWord(self, lp: str, words: List[str]) -> str:
        
        l = [0 for x in range(26)]
        lp = lp.lower()
        print(lp)
        for x in lp:
            if ord('a') <= ord(x) <= ord('z'):
                l[ord(x) - ord('a')]+=1
                
        comp = [[0 for x in range(26)] for y in range(len(words))]
        
        def do_work(indx):
            
            for y in words[indx]:
                comp[indx][ord(y) - ord('a')]+=1
                
        for x in range(len(words)):
            do_work(x)
            
        size = float('inf')
        word = ""
        
        def compare(arr1,arr2):
            
            for x in range(26):
                if arr2[x] > arr1[x]:
                    return False
                
            return True
        
        for x in range(len(comp)):
            if compare(comp[x],l) and len(words[x]) < size:
                size = len(words[x])
                word = words[x]
                
        return word
        
