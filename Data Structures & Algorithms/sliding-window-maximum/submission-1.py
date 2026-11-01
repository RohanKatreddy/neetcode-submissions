class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = {1: nums[:]}

        length = 2
        while length <= k:
            w = length//2
            maximums[length] = [-1] * len(nums)
            for a in range(0, len(nums) - length + 1):
                maximums[length][a] = max(maximums[w][a], maximums[w][a + w])
            length *= 2

        highest_2_power = 1
        while highest_2_power * 2 <= k:
            highest_2_power *= 2
            

        out = []
        for a in range(0, len(nums) - k + 1):
            b = a + k - 1
            out.append(max(maximums[highest_2_power][a], maximums[highest_2_power][b - highest_2_power + 1]))
        
        return out