class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = []

        for num in nums:
            heapq.heappush(sorted_nums, num)
            if len(sorted_nums) > k:
                heapq.heappop(sorted_nums)

        return heapq.heappop(sorted_nums)