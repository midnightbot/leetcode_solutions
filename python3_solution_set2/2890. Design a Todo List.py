class TodoList:

    def __init__(self):
        self.tasks = {}
        self.task_id = 1

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        if userId in self.tasks:
            self.tasks[userId].append([self.task_id, dueDate, tags, taskDescription, 'inc'])
            self.task_id+=1
        else:
            self.tasks[userId] = [[self.task_id, dueDate, tags, taskDescription, 'inc']]
            self.task_id+=1

        return self.task_id-1

    def getAllTasks(self, userId: int) -> List[str]:
        #print(self.tasks, userId)
        temps = []
        if userId in self.tasks:
            temps = self.tasks[userId]
        temp = []
        for ids, date, tags, decp,status in temps:
            if status == 'inc':
                temp.append([decp, date])

        temp = sorted(temp, key = lambda x:x[1])
        temp = [x[0] for x in temp]
        return [x for x in temp]
        
    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        
        if userId in self.tasks:
            temp = self.tasks[userId]

        ans = []
        for ids,date,tags,decp,status in temp:
            if tag in tags and status == 'inc':
                ans.append([decp,date])

        ans = sorted(ans, key = lambda x:x[1])
        ans = [x[0] for x in ans]
        return [x for x in ans]

    def completeTask(self, userId: int, taskId: int) -> None:
        if userId in self.tasks:
            for it in range(len(self.tasks[userId])):
                if self.tasks[userId][it][0] == taskId and self.tasks[userId][it][-1] == 'inc':
                    self.tasks[userId][it][-1] = 'c'

        #print(userId, taskId)
        #print(self.tasks)

# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)
