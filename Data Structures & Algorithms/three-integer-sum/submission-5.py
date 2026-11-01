class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            left_index = i+1
            right_index = len(nums) - 1
            while (left_index < right_index):
                three_sum = nums[i] + nums[left_index] + nums[right_index]
                if three_sum == 0:
                    ans = [nums[i], nums[left_index], nums[right_index]]
                    if ans not in output:
                        output.append(ans)
                    left_index += 1
                if three_sum < 0:
                    left_index += 1
                else: right_index -= 1
        return output