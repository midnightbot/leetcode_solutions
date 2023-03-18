class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines)%n!=0:
            return -1
        balance = sum(machines)//n
        ## always pass the balance of curr machine to the next machine and if still the next machine has less number of clothes borrow it from right side

        ## add flow cost during absorbtion
        ans = 0
        flow_right = 0

        for x in machines:
            flow_right = x + flow_right - balance
            ans = max(ans, abs(flow_right), x - balance)

        return ans
