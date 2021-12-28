##ss
##Solution 1
## DP + Memoization
## (Time Limit Exceeded)
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        comp = list(set(target))
        index = {}
        rev_index = {}
        for x in range(len(comp)):
            index[comp[x]] = x
            rev_index[x] = comp[x]
            
        #print(index)
        useful = []
        for x in range(len(stickers)):
            useful.append(self.find_mask(stickers[x],comp,index))
            
        #print(useful)
        #print(rev_index)
        memo = {}
        targets = self.find_mask(target,comp,index)
        
        self.find_ans(useful,targets,rev_index[0],memo,index,rev_index)
        if memo[self.make_key(targets)] == float('inf'):
            return -1
        return memo[self.make_key(targets)]
    def find_mask(self,sticker,comp,index):
        
        ans = [0 for x in range(len(comp))]
        
        for x in range(len(sticker)):
            if sticker[x] in comp:
                ans[index[sticker[x]]]+=1
                
                
        return ans
    
    def ans_found(self,target):##base case checking
        for x in range(len(target)):
            if target[x] > 0:
                return False
            
            
        return True
    def make_key(self,target):
        ans = ""
        for x in range(len(target)):
            ans+=str(target[x])
            ans+=","
            
        return ans
    def subs(self,sticker,target,rev_index):
        ans = []
        curr = ""
        for x in range(len(target)):
            ans.append(target[x] - sticker[x])
            if ans[x] >0 and len(curr) == 0:
                curr = rev_index[x]
        return ans,curr
    def find_curr(self,target,rev_index):
        ans = ""

        for x in range(len(target)):
            if target[x] > 0:
                ans = str(rev_index[x])
                break
                
        return ans
    def find_ans(self,stickers,target,curr,memo,index,rev_index):
        
        
        if self.ans_found(target):
            return 0
        
        else:
            if self.make_key(target) in memo:
                return memo[self.make_key(target)]
            else:
                mins = float('inf')
                for x in range(len(stickers)):
                    if stickers[x][index[curr]]!=0:
                        new_target,new_curr = self.subs(stickers[x],target,rev_index)
                        #new_curr = self.find_curr(new_target,rev_index)
                        mins = min(mins, 1 + self.find_ans(stickers,new_target,new_curr,memo,index,rev_index))
                        
                        
                memo[self.make_key(target)] = mins
                return memo[self.make_key(target)]
                        
                        
                        
                    
        
