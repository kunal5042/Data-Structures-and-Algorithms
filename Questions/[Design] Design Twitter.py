# Question: https://leetcode.com/problems/design-twitter/
# Medium
from typing import Optional, List

class User:
    def __init__(self, user_id):
        self.id = user_id
        self.following = set()
        self.posts = []
        
    def follows(self, followee):
        self.following.add(followee)
        
    def unfollows(self, followee):
        self.following.discard(followee)
        
    def post(self, timestamp, content):
        self.posts.append((timestamp, content))
        
    def has_any_posts(self):
        return len(self.posts) != 0
        
    def most_recent_post_with_index(self):
        if self.has_any_posts():
            time, content = self.posts[~0]
            return (time, content, len(self.posts)-1)
        
    def __lt__(self, other_user):
        return self.id <= other_user.id
        
from heapq import heapify, heappop, heappush
class Twitter:

    def __init__(self):
        self.time = 0
        self.users = {}

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.time -= 1
        self.signup_check(user_id)
        self.users[user_id].post(self.time, tweet_id)

    def getNewsFeed(self, user_id: int) -> List[int]:
        self.signup_check(user_id)
        feed = []
        heap = []
        
        if self.users[user_id].has_any_posts():
            time, content, index = self.users[user_id].most_recent_post_with_index()
            heap.append((time, content, user_id, index))
            
        for followee in self.users[user_id].following:
            if followee.has_any_posts():
                time, content, index = followee.most_recent_post_with_index()
                heap.append((time, content, followee.id, index))
                
        heapify(heap)
        # greedily breadth-first-search style expanding with respect of timestamp of the post
        while len(heap) != 0 and len(feed) < 10:
            time, content, identification, index_of_post = heappop(heap)
            feed.append(content)
            
            if index_of_post - 1 >= 0:
                time, content = self.users[identification].posts[index_of_post-1]
                heappush(heap, (time, content, identification, index_of_post-1))
                
        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.signup_check(follower_id, followee_id)
        self.users[follower_id].follows(self.users[followee_id])

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.signup_check(follower_id, followee_id)
        self.users[follower_id].unfollows(self.users[followee_id])
    
    def signup_check(self, *user_ids) -> None:
        for user_id in user_ids:
            if user_id not in self.users:
                self.users[user_id] = User(user_id)
        return
'''

# Kunal Wadhwa

'''