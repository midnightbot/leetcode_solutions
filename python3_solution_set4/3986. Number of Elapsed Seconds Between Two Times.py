class Solution:
    def secondsBetweenTimes(self, s: str, e: str) -> int:
        t1 = [int(x) for x in s.split(":")]
        t2 = [int(x) for x in e.split(":")]
        t1 = t1[0]*3600 + t1[1]*60 + t1[2]
        t2 = t2[0]*3600 + t2[1]*60 + t2[2]

        return t2-t1
        
