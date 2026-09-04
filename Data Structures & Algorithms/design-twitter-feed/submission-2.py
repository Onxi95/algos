from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)
        results = []
        for user in self.followers[userId]:
            results.extend(self.tweets[user])
        results.sort(key=lambda xy: xy[0], reverse=True)
        return [tweet for time, tweet in results[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)