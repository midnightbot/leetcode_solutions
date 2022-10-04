##ss
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        ##return min initial energy to finish all tasks
        ##task which are most imbalanced should be done first, hence if task has larger imbalance it can cause problems later, hence deal with them when the energy is max
        
        ##lowest energy required is sum of all actual energy of all tasks
        ##largest energy required is sum of all minimum energy of all tasks
        ##when can now perform binary search to find the least energy that satifies the condition
        low = 0
        high = 0
        tasks = sorted(tasks, reverse = True, key = lambda x:x[1]-x[0])
        
        for x in range(len(tasks)):
            low+=tasks[x][0]
            high+=tasks[x][1]
            
        #high*= len(tasks)*2
        
        while low < high:
            mid = low + (high - low)//2
            #print(low,high,mid,self.isdoable(tasks,mid))
            if self.isdoable(tasks,mid):
                high = mid
                
            else:
                low = mid + 1
                
        return low
        
        
    def isdoable(self,tasks,energy):
        
        for x in range(len(tasks)):
            if energy >= tasks[x][1]:
                energy-=tasks[x][0]
                
            else:
                return False
            
        return True
