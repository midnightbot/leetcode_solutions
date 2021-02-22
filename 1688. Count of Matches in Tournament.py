class Solution:
    def numberOfMatches(self, n: int) -> int:
        currentTeams = n
        matches = 0
        while(currentTeams!=1):
            if currentTeams%2==0:
                matches = matches + (currentTeams/2)
                currentTeams = currentTeams/2
            else:
                matches = matches + (currentTeams-1)/2
                currentTeams = (currentTeams-1)/2+1
                
        return int(matches)
        
