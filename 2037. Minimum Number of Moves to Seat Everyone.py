class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        
        seats = sorted(seats, reverse = False)
        students = sorted(students, reverse = False)

        count = 0
        for x in range (len(seats)):
            count+= abs(seats[x]-students[x])
            
        return count
            
        
