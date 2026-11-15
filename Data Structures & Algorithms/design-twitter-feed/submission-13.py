class Twitter:

    def __init__(self):
        self.users = {} # user id : set of following
        self.tweets = {} # user id : array of tweets (time,tweetId)
        self.time = 0

    # HELPER FUNCTION:
    # Creates entries in class data if userId not available
    def verifyUser(self,userId: int) -> None:

        if userId not in self.users:
            self.users[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = [] # (time, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.verifyUser(userId)
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        lst = []
        heap = []

        self.verifyUser(userId)
        safelist = self.users[userId] | {userId}

        for tweeter in safelist:
            tweets = self.tweets[tweeter]
            if tweets:
                index = len(tweets) - 1
                time,tweetid = tweets[index]
                heapq.heappush(heap,(-time,tweetid,tweeter,index))
        
        while heap and len(lst) < 10:
            time,tweetid,tweeter,index = heapq.heappop(heap)
            lst.append(tweetid)

            # push next most recent tweet into heap
            if index > 0:
                nxtTime, nxtId = self.tweets[tweeter][index-1]
                heapq.heappush(heap,(-nxtTime,nxtId,tweeter,index-1))

        return lst

    def follow(self, followerId: int, followeeId: int) -> None:
        self.verifyUser(followerId)
        self.verifyUser(followeeId)
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.verifyUser(followerId)
        self.verifyUser(followeeId)

        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
