"""
Success
Details 
Runtime: 64 ms, faster than 83.66% of Python3 online submissions for Design Twitter.
Memory Usage: 18.6 MB, less than 22.22% of Python3 online submissions for Design Twitter.
"""
from __future__ import annotations 
import collections 
import random 
import heapq 

# dict + heap 
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0 
        self.follower = collections.defaultdict(set)
        self.tweet = collections.defaultdict(collections.deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        t = (self.timestamp, tweetId)
        self.timestamp += 1 
        self.tweet[userId].appendleft(t)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = {userId} | self.follower.get(userId, set())
        res = []
        count = 0
        max_heap = []

        iter_dict = collections.defaultdict(int)

        for user in users:
            tweet_idx = iter_dict[user]
            tweets = self.tweet[user]
            if tweet_idx < len(tweets):
                t_ts, t_id = tweets[tweet_idx]
                heapq.heappush(max_heap, (-t_ts, user, t_id))

        while max_heap and count < 10:
            t_ts_neg, user, t_id = heapq.heappop(max_heap)
            res.append(t_id)

            iter_dict[user] += 1
            tweets = self.tweet[user]
            tweet_idx = iter_dict[user]
            if tweet_idx < len(tweets):
                t_ts, t_id = tweets[tweet_idx]
                heapq.heappush(max_heap, (-t_ts, user, t_id))

            count += 1

        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)