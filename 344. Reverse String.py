class Solution:
    def reverseString(self, s: List[str]) -> None:
        #print(type(s))
        
        if len(s)%2!=0:
            for x in range(int((len(s)-1)/2)):
                temp = s[x]
                s[x] = s[len(s)-1-x]
                s[len(s)-1-x] = temp
                
        else:
            for x in range(int(len(s)/2)):
                temp = s[x]
                s[x] = s[len(s)-1-x]
                s[len(s)-1-x] = temp
                
        

        
