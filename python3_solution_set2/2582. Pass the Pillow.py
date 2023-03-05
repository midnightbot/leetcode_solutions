class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        rounds = time//(n-1)
        round_direction = (math.floor(time/(n-1)))%2
        rem = time % (n-1)

        #print(rem)
        ##direction l to r
        if round_direction == 0:
            return 1 + rem

        
        ## direction r to l
        else:
            return n - rem
