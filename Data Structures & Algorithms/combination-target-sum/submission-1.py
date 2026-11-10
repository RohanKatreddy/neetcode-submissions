class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.solve([], nums, target)
        return self.res
        

    def solve(self, current, nums, target):
        if target == 0:
            self.res.append(current)
            return
        if not nums: return
        count = 0
        while (nums[0] * count <= target and nums[0] <= target):
            self.solve(current + ([nums[0]] * count), nums[1:], target - (nums[0] * count))
            count += 1