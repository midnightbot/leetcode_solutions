##ss
import heapq
class VideoSharingPlatform:

    def __init__(self):
        self.vids = {} ## vId : [content, views, likes, dislikes]
        self.aval = []
        self.next = 0

    def upload(self, video: str) -> int:
        
        if self.aval:
            top = heapq.heappop(self.aval)
            
        else:
            top = self.next
            self.next+=1
        self.vids[top] = [video,0,0,0]
        return top

    def remove(self, videoId: int) -> None:
        
        if videoId in self.vids:
            self.vids.pop(videoId)
            heapq.heappush(self.aval, videoId)
        

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        
        if videoId in self.vids:
            self.vids[videoId][1]+=1
            return self.vids[videoId][0][startMinute:min(endMinute+1, len(self.vids[videoId][0]))]
        
        return "-1"
            
        
    def like(self, videoId: int) -> None:
        
        if videoId in self.vids:
            self.vids[videoId][2]+=1
        

    def dislike(self, videoId: int) -> None:
        
        if videoId in self.vids:
            self.vids[videoId][3]+=1
        

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        
        if videoId in self.vids:
            return [self.vids[videoId][2], self.vids[videoId][3]]
        
        return [-1]
        

    def getViews(self, videoId: int) -> int:
        
        if videoId in self.vids:
            return self.vids[videoId][1]
        return -1
        


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)
