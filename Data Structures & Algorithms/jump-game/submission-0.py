class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            jumpLength = nums[i]
            possible = goal <= (i + jumpLength)
            if possible:
                goal = i


        return goal <= nums[0]