##ss
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        ## can add one charac [p[0],p[1]] in the text to make longest pattern seq
        
        ##pattern[0] will be added in the beginning
        ##pattern[1] will be added at the end
        ## to make max repetition
        
        
        p1 = 0
        p2 = 0
        
        for x in text:
            if x == pattern[0]:
                p1+=1
                
            if x == pattern[1]:
                p2+=1
                
        ##ans = curr-count + max(p1,p2)
        
        count2 = [0 for x in range(len(text) + 1)]
        
        
        for x in range(len(text)-1,-1,-1):
            if text[x] == pattern[1]:
                count2[x] = count2[x+1] + 1
                
            else:
                count2[x] = count2[x+1]
            
        curr = 0
        
        for x in range(len(text)):
            if text[x] == pattern[0] and pattern[0]!=pattern[1]:
                curr+=count2[x]
                
            elif text[x] == pattern[0] and pattern[0]==pattern[1]:
                curr+=count2[x] - 1
          
        #print(curr,p1,p2)
        if p1!=0 and p2!=0:
            return curr + max(p1,p2)
        
        elif p1==0 and p2==0:
            return 0
        
        elif p1==0 or p2==0:
            return max(p1,p2)
