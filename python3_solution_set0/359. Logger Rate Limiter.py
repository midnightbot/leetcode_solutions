class Logger:

    def __init__(self):
        self.dicts = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.dicts.keys():
            self.dicts[message] = [timestamp]
            return True
        
        else:
            temp = self.dicts[message]
            val = temp[len(temp)-1]
            if timestamp - val < 10:
                #self.dicts[message].append(timestamp)
                return False
            
            else:
                self.dicts[message].append(timestamp)
                return True


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
