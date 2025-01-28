from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        most_recent = []
        min_heap = []

        self.following[userId].add(userId)

        for followee_id in self.following[userId]:
            if followee_id in self.tweets:
                idx = len(self.tweets[followee_id]) - 1
                count, tweet_id = self.tweets[followee_id][idx]
                min_heap.append([count, tweet_id, followee_id, idx - 1])
        
        heapq.heapify(min_heap)

        while min_heap and len(most_recent) < 10:
            _, tweet_id, followee_id, idx = heapq.heappop(min_heap)
            most_recent.append(tweet_id)

            if idx >= 0:
                count, tweet_id = self.tweets[followee_id][idx]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, idx - 1])
        
        return most_recent

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
