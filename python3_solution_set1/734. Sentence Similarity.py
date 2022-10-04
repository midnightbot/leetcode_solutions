##ss
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1)!=len(sentence2):
            return False
        
        for x in range(len(sentence1)):
            temp1 = [sentence1[x],sentence2[x]]
            temp2 = temp1[::-1]
            
            if temp1 not in similarPairs and temp2 not in similarPairs and sentence1[x]!=sentence2[x]:
                return False
            
        return True
