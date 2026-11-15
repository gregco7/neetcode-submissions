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
        self.tweets = [] # (tweet id, user id) tweets, least recent -> most recent, 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.users:
            self.users[userId] = set()
        self.tweets.append((tweetId,userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetches at most the 10 most recent tweet ids in the users news feed
        # each item must be posted by users who the user is following or by the user themself.
        # tweet ids should be ordered from most recent to least recent
        lst = []
        if not userId in self.users:
            return lst

        followset = self.users[userId]
        aggregate = 0
        
        for i in range(len(self.tweets) - 1,-1,-1):
            tweet = self.tweets[i]
            if ((tweet[1] == userId) or (tweet[1] in followset)):
                lst.append(tweet[0])
                aggregate += 1
                if aggregate == 10:
                    break
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

