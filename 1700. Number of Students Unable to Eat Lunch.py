##ss
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        c = 0
        n = len(students)
        while c < n*n and len(students)!=0:
            c+=1
            
            #print(students)
            if students[0] == sandwiches[0]:
                students = students[1:len(students)]
                sandwiches = sandwiches[1:len(sandwiches)]
                
                
            else:
                temp = students[0]
                students = students[1:len(students)]
                students.append(temp)
        
        
        return len(students)
