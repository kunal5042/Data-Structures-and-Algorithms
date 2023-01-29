# Question: https://leetcode.com/problems/tweet-counts-per-frequency/
# Medium
from typing import Optional, List

class TweetCounts:

    def __init__(self):
        self.hash = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.hash[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute': x = 60
        if freq == 'hour'  : x = 3600
        if freq == 'day'   : x = 86400
        tweets = []
        while startTime <= endTime:
            y = min(startTime + x, endTime + 1)
            tweets.append(bisect_left(self.hash[tweetName], y) - bisect_left(self.hash[tweetName], startTime))
            startTime += x
        return tweets


# January 29, 2023

'''

# Kunal Wadhwa

'''