class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        curr = ''
        
        for indx,x in enumerate(num):
            if x!='0':
                return num[indx:][::-1]
        return ''
            
        
