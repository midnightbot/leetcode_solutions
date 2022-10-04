##ss
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        temp = sentence.split(" ")
        print(temp)
        
        for x in range(len(temp)):
            if temp[x][0] in ['a','e','i','o','u','A','E','I','O','U']:
                
                temp[x] = temp[x] + 'ma' + ''.join(['a' for n in range(x+1)])
                
                    
                
            else:
                temp[x] = temp[x][1:] + temp[x][0] + 'ma' + ''.join(['a' for n in range(x+1)])
                
        return ' '.join(temp)
