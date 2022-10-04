##ss
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        emp = []
        #print(len(schedule))
        for x in range(len(schedule)):
            if len(schedule[x]) == None:
                break
            else:
                #print(len(schedule[x]))
                for y in range(len(schedule[x])):
                    emp.append((schedule[x][y].start,schedule[x][y].end))
        
       # print(emp)
        
        emp = sorted(emp, key = lambda x:x[0])
        #print(emp)
        ans = []
       
        last_time = emp[0][1]
        for x in range(1,len(emp)):
            if emp[x][0] > last_time:
                #print("hi")
                ans.append(Interval(last_time,emp[x][0]))
                last_time = max(last_time,emp[x][1])
            last_time = max(last_time,emp[x][1])   
        #print(ans)   
        #ans = [Interval(0,1)]
        return ans
        #return emp
