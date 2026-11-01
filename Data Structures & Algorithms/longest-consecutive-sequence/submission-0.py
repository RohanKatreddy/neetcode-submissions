class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        maximum_length = 1
        current_length = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i]-1 == nums[i-1]:
                current_length += 1
            else:
                maximum_length = max(maximum_length, current_length)
                current_length = 1
        maximum_length = max(maximum_length, current_length)
        return maximum_length