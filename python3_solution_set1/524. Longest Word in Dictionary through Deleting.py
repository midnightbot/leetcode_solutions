##ss
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        dictionary = sorted(dictionary)
        dictionary = sorted(dictionary,reverse = True,key = lambda x:len(x))
        #print(dictionary)
        ##sorted acc to length and lexical order
        
        for x in range(len(dictionary)):
            i = 0
            j = 0
            while i < len(dictionary[x]) and j < len(s):
                if dictionary[x][i] == s[j]:
                    i+=1
                    
                j+=1
                
            if i == len(dictionary[x]):
                return dictionary[x]
            
        return ""
        
