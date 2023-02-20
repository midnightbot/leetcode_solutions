import math
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:

        ## state = 0 (enter)  state = 1 (exit)

        ## door not used in prev seconds : exit goes first
        ## door used for entering in prev second : enter goes first
        ## door used for exit in prev second : exit goes first
        ## multiple person want to go in same direction, person will small index goes
        
        ## simple two stack question
        ## ss
        n = len(state)
        ans = [0 for x in range(n)]

        enter = []
        out = []
        status = 0
        ## 0 (unused)  1 (enter)  -1(exit)
        time = 0
        done = 0
        for x in range(n):
            if state[x] == 0:
                enter.append([arrival[x], x])
            else:
                out.append([arrival[x],x])

        #enter = enter[::-1]
        #out = out[::-1]
        enter.append([float('inf'), float('inf')])
        out.append([float('inf'), float('inf')])

        while done!=n:
            option1, indx1 = enter[0][0], enter[0][1]
            option2, indx2 = out[0][0], out[0][1]

            if option1 <= time and option2 > time:
                status = 1
                ans[indx1] = time
                enter.pop(0)
                time+=1
                done+=1

            elif option1 > time and option2<= time:
                status = -1
                ans[indx2] = time
                out.pop(0)
                time+=1
                done+=1

            elif option1<= time and option2<=time:
                if status == 0 or status == -1:
                    status = -1
                    ans[indx2] = time
                    out.pop(0)

                elif status == 1:
                    status = 1
                    ans[indx1] = time
                    enter.pop(0)
                time+=1
                done+=1
            else:
                status = 0
                time = min(option1, option2)
        return ans
