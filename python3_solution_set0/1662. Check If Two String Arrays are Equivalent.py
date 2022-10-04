class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        
        for x in range(len(word1)):
            str1+=word1[x]
            
        for y in range(len(word2)):
            str2+=word2[y]
            
        print(str1)
        print(str2)
        if str1 == str2:
            return True
        else:
            return False
        
