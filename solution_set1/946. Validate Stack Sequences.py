##ss
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        i = 0
        j = 0
        
        stack = []
        
        
        
        while j < len(popped) and i < len(pushed):
            #print(i,j,stack)
            if len(stack) == 0 and popped[j] in pushed[i:]:
                indx = pushed[i:].index(popped[j])
                k = i
                while k <= indx + i:
                    stack.append(pushed[k])
                    k+=1
                    
                i = k
            elif len(stack) ==0 and popped[j] not in pushed[i:]:
                return False
                
            elif len(stack)!=0 and stack[-1]!=popped[j] and popped[j] in pushed[i:]:
                indx = pushed[i:].index(popped[j])
                k = i
                #print(indx)
                #print("insdie")
                while k <= indx + i:
                    stack.append(pushed[k])
                    k+=1
                    
                i = k
                    
            elif stack[-1] == popped[j]:
                stack.pop()
                j+=1
                
            elif stack[-1]!=popped[j] and popped[j] not in pushed[i:]:
                return False
            
        for x in range(j,len(popped)):
            if stack[-1]!=popped[x]:
                return False
            
            else:
                stack.pop()
                
        return True

            #print(stack)
        
