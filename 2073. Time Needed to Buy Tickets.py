class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ans  = 0
        n = tickets[k]
        for x in range(k):
            ans+= min(tickets[x],n)
        
        for x in range(k+1,len(tickets)):
            ans+=min(tickets[x],n-1)
            
        return ans+n
