class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums[1:])
        for i in range(len(nums)):
            if (target - nums[i]) in s:
                for j in range(i+1, len(nums)):
                    if nums[j] == (target-nums[i]):
                        return [i, j]