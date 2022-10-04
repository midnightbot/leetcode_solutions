##ss
##Solution 1 (Union Find) Time Limit Exceeded
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings = sorted(meetings,key = lambda x:(x[2],-x[1],-x[0]))
        ans = set()
        
        #print(meetings)
        self.roots = [x for x in range(n)]
        self.roots[firstPerson] = 0
        ans.add(0)
        ans.add(firstPerson)
        
        grps = [meetings[0]]
        for x in range(1,len(meetings)):
            if meetings[x][2] == meetings[x-1][2]:
                grps.append(meetings[x])
                
            else:
                var = True
                notseen = []
                while var:
                    var = False
                    for z in grps:
                        if self.find(z[0]) == 0 or self.find(z[1]) == 0 and (self.find(z[0])!=0 or self.find(z[0])!=0):
                            var = True
                            ans.add(z[0])
                            ans.add(z[1])
                            self.roots[z[0]] = 0
                            self.roots[z[1]] = 0
                        else:
                            notseen.append(z)
                            
                    grps = notseen
                    notseen = []
                    
                grps = [meetings[x]]
                
        var = True
        notseen = []
        while var:
            var = False
            for z in grps:
                if self.find(z[0]) == 0 or self.find(z[1]) == 0 and (self.find(z[0])!=0 or self.find(z[0])!=0):
                    var = True
                    ans.add(z[0])
                    ans.add(z[1])
                    self.roots[z[0]] = 0
                    self.roots[z[1]] = 0
                    
                else:
                    notseen.append(z)
                    
            grps = notseen
            notseen = []
                

                
        return ans

        
        
    def find(self,v): ##returns which group does an element belong to
        #print(v)
        if self.roots[v]!=v:
            self.roots[v] = self.find(self.roots[v])

        return self.roots[v]


    def union(self,u,v): ## merges two groups
        p1 = self.find(u)
        p2 = self.find(v)

        if p1!=p2 and (p1==0 or p2==0) and (p1!=0 or p2!=0):
            self.roots[p2] = 0
            self.roots[p1] = 0
            return True

        return False
        
        
 ## Solution 2 (usind deque)
from collections import deque
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings = sorted(meetings,key = lambda x:(x[2]))
        ans = set()
        frames = {}
        
        #print(meetings)
        self.roots = [x for x in range(n)]
        self.roots[firstPerson] = 0
        ans.add(0)
        ans.add(firstPerson)
        
        grps = [meetings[0]]
        for x in range(1,len(meetings)):
            if meetings[x][2] == meetings[x-1][2]: ## grp all meetings that have same time
                grps.append(meetings[x])
                
            else:
                thisgrp = deque(grps)
                l = len(thisgrp)
                while thisgrp and l>0: ##solving all meetings that have same time
                    meet = thisgrp.pop()
                    if meet[0] not in ans and meet[1] not in ans:
                        thisgrp.appendleft(meet)
                        l-=1
                        
                    else:
                        ans.add(meet[0])
                        ans.add(meet[1])
                        l = len(thisgrp)
                
                grps = []
                grps.append(meetings[x])
        
        thisgrp = deque(grps)
        l = len(thisgrp)
        while thisgrp and l>0:
            meet = thisgrp.pop()
            if meet[0] not in ans and meet[1] not in ans:
                
                thisgrp.appendleft(meet)
                l-=1
                        
            else:
                ans.add(meet[0])
                ans.add(meet[1])
                l = len(thisgrp)
                
        
                

                
        return ans

        
        
    def find(self,v): ##returns which group does an element belong to
        #print(v)
        if self.roots[v]!=v:
            self.roots[v] = self.find(self.roots[v])

        return self.roots[v]


    def union(self,u,v): ## merges two groups
        p1 = self.find(u)
        p2 = self.find(v)

        if p1!=p2 and (p1==0 or p2==0) and (p1!=0 or p2!=0):
            self.roots[p2] = 0
            self.roots[p1] = 0
            return True

        return False
        
