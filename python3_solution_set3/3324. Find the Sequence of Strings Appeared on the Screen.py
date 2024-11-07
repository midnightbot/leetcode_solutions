class Solution:
    def stringSequence(self, target: str) -> List[str]:
        # simple iteration

        def find_next(s):
            return chr((ord(s)-ord('a')+1)%26 + ord('a'))
        ans = []
        for x in range(len(target)):
            if target[x] == 'a':
                ans.append(target[:x+1])
            else:
                for y in range(ord(target[x])-ord('a')+1):
                    ans.append(target[:x] + chr(ord('a')+y))
        return ans
        
        
