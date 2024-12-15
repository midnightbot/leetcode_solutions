class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:

        for x in range(len(events)):
            if x == 0:
                events[0].append(events[0][1])

            else:
                events[x].append(events[x][1] - events[x-1][1])
            
            events[x].append(x)
        
        events = sorted(events, key = lambda x:(-x[2],x[0]))
        return events[0][0]
