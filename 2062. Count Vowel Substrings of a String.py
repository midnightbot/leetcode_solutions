##ss
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        ans = 0
        compare = set()
        compare.add('a')
        compare.add('e')
        compare.add('i')
        compare.add('o')
        compare.add('u')
        
        if len(word) < 5:
            return 0
        
        else:
            for x in range(0,len(word)-4):
                #print("inside")
                temp = set()
                
                for y in range(x,len(word)):
                    temp.add(word[y])
                    if len(temp)>=5 and temp!=compare:
                        break
                    elif temp == compare:
                        #print(temp)
                        ans+=1
                
                #print(temp)
                
                    
            return ans
                    
                    
        
        
