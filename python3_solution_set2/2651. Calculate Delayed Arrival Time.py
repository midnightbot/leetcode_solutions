class Solution:
    def findDelayedArrivalTime(self, at: int, dt: int) -> int:

        return (at+dt)%24
