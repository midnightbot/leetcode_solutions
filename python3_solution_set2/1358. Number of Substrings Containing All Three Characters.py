class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        def valid(arr): ## to check if substring is valid
            for x in arr:
                if x == 0:
                    return False

            return True

        i = 0
        j = 0
        n = len(s)
        curr = [0,0,0] ##acount, bcount, ccount

        ans = 0
        while j < len(s):
            if valid(curr):
                ans+= n-j+1

                while valid(curr): ## pop from left side till it is invalid
                    curr[ord(s[i])-ord('a')]-=1
                    ans+=(n-j+1)
                    i+=1
                ans-=(n-j+1)
            curr[ord(s[j])-ord('a')]+=1
            j+=1
            #print(ans, curr)

        while valid(curr): ## pop from left side till it is invalid
            curr[ord(s[i])-ord('a')]-=1
            ans+=1
            i+=1
        #print(curr)
        
                
            
        return ans
