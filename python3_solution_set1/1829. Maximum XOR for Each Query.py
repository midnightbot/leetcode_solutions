##ss
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        ans = []
        pre = [nums[0]]
        maxs = 2 ** maximumBit - 1
       
        # print(maxs)
        for x in range(1,len(nums)):
            pre.append(pre[-1] ^ nums[x])
            
        # print(0 ^ 3)\
        #print(pre)
        pre = pre[::-1]
        #print(pre)
        for x in range(len(pre)):
            curr = pre[x]
            temp = format(curr, "b")
            # print(len(temp),temp)
            #print(curr,temp)
            if len(temp) < maximumBit:
                #ans.append(maxs)
                t1 = [1 for z in range(maximumBit)]
                t2 = [z for z in temp]
                t2 = [int(z) for z in t2]
                t1 = t1[::-1]
                t2 = t2[::-1]
                
                for it in range(len(t2)):
                    if t2[it] == 1:
                        t1[it] = 0
                        
                t1 = t1[::-1]
                #print(t1,curr)
                t1 = [str(h) for h in t1]
                ans.append(int(''.join(t1),2))
                
            else:
                t1 = [1 for z in range(maximumBit)]
                t2 = [z for z in temp]
                t2 = [int(z) for z in t2]
                t1 = t1[::-1]
                t2 = t2[::-1]
                
                for it in range(len(t1)):
                    if t2[it] == 1:
                        t1[it] = 0
                        
                t1 = t1[::-1]
                #print(t1,curr)
                t1 = [str(h) for h in t1]
                ans.append(int(''.join(t1),2))
                #ans.append("*")
                
        #print(pre)
        return ans
        
