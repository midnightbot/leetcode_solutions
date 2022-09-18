class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        set1 = set()
        days = [-1,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def find_start_point(m,d):
            ans = 0
            for x in range(1,m):
                ans+=days[x]
            ans+=d
            
            return ans
        
        a = arriveAlice.split("-")
        a = [int(x) for x in a]
        
        b = leaveAlice.split("-")
        b = [int(x) for x in b]
        
        c = arriveBob.split("-")
        c = [int(x) for x in c]
        
        d = leaveBob.split("-")
        d = [int(x) for x in d]
        
        
        start1,end1 = find_start_point(a[0],a[1]), find_start_point(b[0],b[1])
        
        start2,end2 = find_start_point(c[0],c[1]), find_start_point(d[0],d[1])
        #print(start1, start2)
        set1 = set()
        set2 = set()
        for x in range(start1, end1 + 1):
            set1.add(x)
            
        for x in range(start2, end2 + 1):
            set2.add(x)
        
        set1 = set1.intersection(set2)
        return len(set1)
