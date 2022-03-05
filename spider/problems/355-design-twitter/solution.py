class Twitter:

    def __init__(self):
        self.tls=[]
        self.fls=[]


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tls.append((userId,tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        f =[fe for fr,fe in self.fls if fr==userId] +[userId]
        nli=[]
        for i in range(len(self.tls)-1,-1,-1):
            u,t = self.tls[i]
            if len(nli)>=10:break
            if u in f: nli.append(t)
        return nli

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fls.append((followerId,followeeId))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId,followeeId) in self.fls: self.fls.remove((followerId,followeeId))



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)