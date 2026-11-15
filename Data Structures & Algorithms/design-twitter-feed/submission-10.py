class Twitter:

    # user
    # - following ids
    # - their tweets

    def __init__(self):
        # implement a verion of twitter which allowed users to
        # post tweets
        # follow/unfollow each other
        # view the 10 most recent tweets within their own news feed
        # users and tweets are uniquely identified by their IDs (integers).
        self.users = {} # user id:  set(),  user id, set of those they follow
        self.tweets = {} # user id : [(time, tweetid)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.users:
            self.users[userId] = set()
        if not userId in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetches at most the 10 most recent tweet ids in the users news feed
        # each item must be posted by users who the user is following or by the user themself.
        # tweet ids should be ordered from most recent to least recent
        lst = []
        heap = []
        
        safelist = self.users[userId] | {userId} if userId in self.users else {userId}


        for tweeter in safelist:
            if tweeter in self.tweets and self.tweets[tweeter]:
                index = len(self.tweets[tweeter]) - 1
                time, tweetId = self.tweets[tweeter][index]
                heapq.heappush(heap, (-time, tweetId, tweeter, index))
        
        while heap and len(lst) < 10:
            negTime, tweetId, tweeter, index = heapq.heappop(heap)
            lst.append(tweetId)

            if index > 0:
                ntime, ntweetId = self.tweets[tweeter][index-1]
                heapq.heappush(heap,(-ntime, ntweetId, tweeter, index - 1))
        return lst

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.users[followerId] = set()
        
        self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            return None
        else:
            if followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)
            else:
                return None

