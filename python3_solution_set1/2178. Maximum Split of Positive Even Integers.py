##ss
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        stack = []
        if finalSum%2!=0:
            return []
        
        else:
            #return []
            while finalSum!=0:
                #print(stack)
                if len(stack) == 0:
                    stack.append(2)
                    finalSum-=2
                    
                elif stack and stack[-1]+2 <= finalSum:
                    stack.append(stack[-1]+2)
                    finalSum-=stack[-1]
                    
                elif stack and stack[-1] + 2 > finalSum:
                    t = stack.pop()
                    finalSum+=t
                    stack.append(finalSum)
                    finalSum = 0
                    
                #print(stack)
            return stack
                    
                
        
