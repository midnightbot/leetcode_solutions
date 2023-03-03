class Solution:
    def maxValue(self, num: str, x: int) -> str:

        ## maximize the value

        if num[0]!='-':
            ans = ''
            added = False
            for it in range(len(num)):
                if int(num[it]) < x:
                    ans+=str(x)
                    ans+=num[it:]
                    added = True
                    break
                
                else:
                    ans+=num[it]

            if added == False:
                return ans+str(x)
            return ans

        else:
            ans = '-'
            added = False
            for it in range(1,len(num)):
                if int(num[it]) > x:
                    ans+=str(x)
                    ans+=num[it:]
                    added = True
                    break
                
                else:
                    ans+=num[it]

            if added == False:
                return ans+str(x)
            return ans
        
