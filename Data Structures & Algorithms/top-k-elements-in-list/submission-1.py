class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict: dict[num] += 1
            else: dict[num] = 1
        
        return [val for val, _ in sorted(list(dict.items()), key=lambda x: x[1])[-k:]]