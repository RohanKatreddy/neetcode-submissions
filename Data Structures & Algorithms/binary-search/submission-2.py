class Solution:
    def search(self, nums: List[int], target: int) -> int:
        step_size = len(nums)-1
        i = 0
        while (step_size > 0):
            if (i + step_size) >= len(nums) or nums[i + step_size] > target:
                step_size //= 2
            else: i += step_size

        return i if nums[i] == target else -1