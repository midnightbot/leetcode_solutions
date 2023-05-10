class FrequencyTracker:
    def __init__(self):
        self.nums = {}  ## contains number and its freq count
        self.freq = {}  ## contains frequncy and all numbers with that freq
        
    def add(self, number: int) -> None:
        og_freq = self.nums.get(number,0)
        self.nums[number] = og_freq + 1
        if og_freq == 0:
            if 1 in self.freq:
                self.freq[1].append(number)
            else:
                self.freq[1] = [number]

        else:
            self.freq[og_freq].remove(number)
            if og_freq+1 in self.freq:
                self.freq[og_freq+1].append(number)
            else:
                self.freq[og_freq+1] = [number]

    def deleteOne(self, number: int) -> None:
        if number in self.nums and self.nums[number]!=0:
            og_freq = self.nums[number]
            self.nums[number]-=1

            self.freq[og_freq].remove(number)
            if og_freq-1 in self.freq:
                self.freq[og_freq-1].append(number)
            else:
                self.freq[og_freq-1] = [number]
    def hasFrequency(self, f: int) -> bool:
        return f in self.freq and len(self.freq[f])!=0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
