class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s_prev = "-1"
        count = 0
        while s!=s_prev:
            new_s = ""
            it = 0
            count+=1
            while it < len(s)-1:
                if s[it] == '1':
                    new_s+="1"
                    it+=1;
                else:
                    if s[it+1] == '0':
                        new_s+='0'
                        it+=1
                    else:
                        new_s+='10'
                        it+=2
            if it != len(s):
                new_s+=s[-1]
                
            s_prev = s
            s = new_s
            #print(s)
                
        return count-1
        
