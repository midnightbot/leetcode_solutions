##ss
class Twitter:

    def __init__(self):
        self.posts = {} ## key-person_id  val:[post_id,time]
        self.follows = {} ##key -person_id  val: list of people who he follow
        self.time = 0
        #print("a")
    def postTweet(self, userId: int, tweetId: int) -> None:
        
        if userId in self.posts:
            self.posts[userId].append([tweetId,self.time])
            
        else:
            self.posts[userId] = [[tweetId,self.time]]
            
        self.time+=1
        #print("b")
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        #print('c')
        post_ent = []
        if userId in self.follows:
            for x in self.follows[userId]:
                if x in self.posts:
                    if len(self.posts[x]) <= 10:
                        for y in self.posts[x]:
                            post_ent.append(y)

                    else:
                        for y in range(len(self.posts[x])-10,len(self.posts[x])):
                            post_ent.append(self.posts[x][y])
                            
                            
        if userId in self.posts:
            if len(self.posts[userId]) <= 10:
                for y in self.posts[userId]:
                    post_ent.append(y)

            else:
                for y in range(len(self.posts[userId])-10,len(self.posts[userId])):
                    post_ent.append(self.posts[userId][y])
                    
        #print(post_ent)           
        post_ent = sorted(post_ent, reverse=True, key = lambda x:x[1])
        ans = []
        for z in range(0,min(len(post_ent),10)):
            ans.append(post_ent[z][0])
        
        if len(ans) == 0:
            return None
        return ans
        #return [1,0]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
            
        else:
            self.follows[followerId] = {followeeId}
        #print("d")
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        #a = 1
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        #print("e")
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
