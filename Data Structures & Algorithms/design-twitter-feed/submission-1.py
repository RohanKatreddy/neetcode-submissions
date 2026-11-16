class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)
        self.posts[userId].append((-self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        limit = 10
        following = self.following[userId]
        result = []

        kth_post = -1
        while True:
            for followee in following:
                if len(self.posts[followee]) >= -kth_post:
                    heapq.heappush(heap, self.posts[followee][kth_post])

            if limit <= 0 or len(heap) == 0:
                return result
            else:
                result.append(heapq.heappop(heap)[1])
                limit -= 1
                kth_post -= 1


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]: return None
        self.following[followerId].remove(followeeId)
