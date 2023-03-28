class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key = lambda x:x[1])
        ans = 0
        curr = [intervals[0][1]-1, intervals[0][1]]
        #print(curr)
        ## always try to use the last 2 elements of the range

        ## if the next range start that these two no need to add more elements
        ## if start is far from the max(curr) we need to add more elements in the ans
        
        for start,end in intervals[1:]:
            if start > curr[1]:
                ans+=2
                curr = [end-1,end]

            elif start > curr[0]:
                ans+=1 
                if curr[1] == end:
                    curr = [end-1,end]
                else:
                    curr = [curr[1], end]
            #print(curr)

        return ans+2

