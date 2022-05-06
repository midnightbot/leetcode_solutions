class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1]+=1
                
                
            else:
                stack.append([x,1])

        
        
        result = ""
        
        for x,count in stack:
            result += ''.join([x for z in range(count)])
            
        return result
