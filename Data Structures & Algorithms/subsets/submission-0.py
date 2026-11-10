class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        for i in range(len(nums)+1):
            combinations.extend(self.subsetsOfK([], nums, i))

        return combinations
        

    def subsetsOfK(self, curr, nums, length):
        if len(curr) == length: return [curr]
        if not nums: return []
        combinations = []
        combinations.extend(self.subsetsOfK(curr+[nums[0]], nums[1:], length))
        combinations.extend(self.subsetsOfK(curr, nums[1:], length))
        return combinations